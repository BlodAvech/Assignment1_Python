# Library Management System

def display_menu():
    """Displays the main menu."""
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. Search for a Book")
    print("3. View All Books")
    print("4. Exit")

def get_positive_integer(x):
    while True:
        try:
            value = int(input(x))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def add_book(books):
    title = input("Enter the title: ").strip()
    author = input("Enter the author: ").strip()
    year = get_positive_integer("Enter the year of publication: ")
    copies = get_positive_integer("Enter the number of copies: ")

    for book in books:
        if book['title'].lower() == title.lower():
            book['copies_available'] += copies
            print(f"Updated the number of copies for '{title}'.")
            return

    books.append({
        "title": title,
        "author": author,
        "year": year,
        "copies_available": copies
    })
    print(f"Added '{title}' to the library.")

def search_book(books):
    title = input("Enter the title to search: ").strip()
    for book in books:
        if book['title'].lower() == title.lower():
            print(f"\nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\nCopies Available: {book['copies_available']}\n")
            return
    print("The book was not found.")

def view_all_books(books):
    if not books:
        print("No books available in the library.")
        return

    print(f"{'Title':<20}{'Author':<20}{'Year':<10}{'Copies'}")
    print("-" * 60)
    for book in books:
        print(f"{book['title']:<20}{book['author']:<20}{book['year']:<10}{book['copies_available']}")

def main():
    books = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            search_book(books)
        elif choice == "3":
            view_all_books(books)
        elif choice == "4":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()