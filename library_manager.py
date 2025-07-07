# Import necessary modules
import json  # For handling JSON file operations
import os    # For checking file existence

"""
FUNCTION DEFINITIONS SECTION
All the helper functions for our library manager are defined here
"""

def display_menu():
    """
    Displays the main menu options to the user
    This function doesn't take any parameters or return anything
    It just prints the menu options
    """
    print("\nPersonal Library Manager")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

   

def add_book(library):
    """
    Adds a new book to the library (which is a list of dictionaries)
    Takes the library list as parameter and modifies it by adding a new book
    """
    print("\nAdd a New Book")
    
    # Get book details from user with input validation
    
    # Title and author don't need special validation
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    
    """
    INPUT VALIDATION LOOP for publication year
    This while loop continues until we get valid integer input
    """
    while True:
        try:
            year = int(input("Enter publication year: "))
            # Additional validation - year should be positive and not in future
            if year < 0 or year > 2025:
                print("Please enter a valid year.")
                continue  # Skip rest of loop and start again
            break  # Exit loop if we get valid input
        except ValueError:  # Handle case where input isn't a number
            print("Please enter a valid year number.")
    
    genre = input("Enter genre: ").strip()
    
    """
    INPUT VALIDATION LOOP for read status
    Another while loop for yes/no validation
    """
    while True:
        read_status = input("Have you read this book? (y/n): ").lower()
        if read_status in ['y', 'n']:  # Check if input is valid
            break
        print("Please enter 'y' or 'n'.")
    
    # Create a book dictionary with all the collected information
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read_status == 'y'  # Convert y/n to boolean
    }
    
    # Add the new book dictionary to our library list
    library.append(book)
    print(f"\nBook '{title}' added successfully!")

def remove_book(library):
    """
    Removes a book from the library by title
    Takes the library list as parameter and modifies it
    """
    # First check if library is empty
    if not library:  # This is equivalent to if len(library) == 0
        print("\nThe library is empty!")
        return  # Exit function early if no books
    
    title = input("\nEnter the title of the book to remove: ").strip()
    found = False  # Flag to track if we found the book
    
    """
    ITERATING THROUGH LIBRARY WITH FOR LOOP
    We use library[:] to create a copy for iteration to avoid issues
    when modifying the list while iterating
    """
    for book in library[:]:  # The [:] creates a slice copy of the list
        # Case-insensitive comparison
        if book['title'].lower() == title.lower():
            library.remove(book)
            print(f"Book '{title}' removed successfully!")
            found = True
            break  # Exit loop after first match
    
    # Check if we didn't find the book
    if not found:
        print(f"No book with title '{title}' found in the library.")

def search_books(library):
    """
    Searches for books by title or author (case-insensitive)
    Takes library as parameter but doesn't modify it
    """
    if not library:
        print("\nThe library is empty!")
        return
    
    search_term = input("\nEnter title or author to search for: ").strip().lower()
    results = []  # List to store matching books
    
    """
    SEARCH LOOP - Checking each book for matches
    """
    for book in library:
        # Check if search term appears in title or author (case-insensitive)
        if (search_term in book['title'].lower() or 
            search_term in book['author'].lower()):
            results.append(book)  # Add matching book to results
    
    # Display results if any found
    if results:
        print(f"\nFound {len(results)} matching book(s):")
        display_book_list(results)
    else:
        print("\nNo matching books found.")

def display_all_books(library):
    """
    Displays all books in the library in formatted way
    """
    if not library:
        print("\nThe library is empty!")
        return
    
    print(f"\nAll Books in Library ({len(library)} total):")
    display_book_list(library)

def display_book_list(books):
    """
    Helper function to display a list of books in formatted way
    Takes a list of book dictionaries as parameter
    """
    """
    ENUMERATED FOR LOOP - we use enumerate to get both index and book
    The 1 as second argument makes numbering start at 1 instead of 0
    """
    for i, book in enumerate(books, 1):
        # Ternary expression to convert boolean to "Read"/"Unread"
        read_status = "Read" if book['read'] else "Unread"
        
        # Formatted output using f-strings
        print(f"\n{i}. {book['title']} by {book['author']}")
        print(f"   Year: {book['year']}, Genre: {book['genre']}, Status: {read_status}")

def display_statistics(library):
    """
    Calculates and displays library statistics
    """
    if not library:
        print("\nThe library is empty!")
        return
    
    total_books = len(library)
    # Count read books using generator expression
    read_books = sum(1 for book in library if book['read'])
    # Calculate percentage with protection against division by zero
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    
    print("\nLibrary Statistics:")
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books} ({percentage_read:.1f}%)")
    print(f"Books unread: {total_books - read_books}")

def save_library(library, filename='library.json'):
    """
    Saves the library to a JSON file
    Uses exception handling in case of file errors
    """
    try:
        with open(filename, 'w') as f:
            json.dump(library, f)  # Write library list as JSON
        print(f"\nLibrary saved to {filename}")
    except Exception as e:  # Catch any error that might occur
        print(f"\nError saving library: {e}")

def load_library(filename='library.json'):
    """
    Loads the library from a JSON file if it exists
    Returns empty list if file doesn't exist or error occurs
    """
    try:
        if os.path.exists(filename):  # Check if file exists
            with open(filename, 'r') as f:
                return json.load(f)  # Load and return library data
    except Exception as e:  # Catch any error that might occur
        print(f"\nError loading library: {e}")
    return []  # Return empty list if no file or error

"""
MAIN PROGRAM SECTION
This is where the program execution starts
"""
def main():
    """
    Main function that runs the library manager
    Contains the main program loop
    """
    # Load existing library or create empty one
    library = load_library()
    print("Welcome to the Personal Library Manager!")
    
    """
    MAIN PROGRAM LOOP
    This while loop runs until user chooses to exit
    """
    while True:
        display_menu()  # Show menu options
        choice = input("\nEnter your choice (1-6): ").strip()
        
        """
        MENU OPTION HANDLING WITH IF-ELIF CHAIN
        Each option calls the appropriate function
        """
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            # Save before exiting
            save_library(library)
            print("\nThank you for using the Personal Library Manager. Goodbye!")
            break  # Exit the while loop
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

# This standard Python idiom checks if we're running this file directly
if __name__ == "__main__":
    main()  # Start the program