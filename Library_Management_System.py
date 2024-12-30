# Library_Management_System.py

import library_module as lm

def main():
    while True:
        books = lm.load_books()
        members = lm.load_members()
        print("\n--- Library Management System ---")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Issue a book")
        print("4. Return a book")
        print("5. Add a new book")
        print("6. View all members")
        print("7. Register a new member")
        print("8. Exit")

        choice = input("Enter your choice (1-8) - ")

        if choice == '1' :
            lm.view_books(books)

        elif choice == '2':
            search_method = input("Choose search method (1 for Linear, 2 for Binary): ")
            title = input("Enter book title to search: ")

            if search_method == '1':
                book = lm.linear_search_books(books, title)
            else:
                book = lm.binary_search_books(books, title)

            if book:
                print("\nBook Found:")
                print(f"ID: {book['id']}")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Available Copies: {book['available_copies']}")
            else:
                print("Book not found.")

        elif choice == '3' :
            book_id = input("Enter book ID to issue: ")
            member_id = input("Enter member ID: ")
            lm.issue_book(books, members, book_id, member_id)

        elif choice == '4' :
            book_id = input("Enter book ID to return: ")
            member_id = input("Enter member ID: ")
            lm.return_book(books, members, book_id, member_id)
            
        elif choice == '5' :
            lm.add_book(books)

        elif choice == '6' :
            lm.view_members(members)

        elif choice == '7':
            lm.register_member(members)

        elif choice == '8' :
            print("Exiting Library Management System...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
