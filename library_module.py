# library_module.py

def load_books() :
    """To load books from books.txt"""
    books = []
    try:
        with open('books.txt', 'r') as file:
            for line in file:
                book_data = line.strip().split(',')
                books.append({
                    'id': book_data[0].strip(),
                    'title': book_data[1].strip(),
                    'author': book_data[2].strip(),
                    'total_copies': int(book_data[3].strip()),
                    'available_copies': int(book_data[4].strip())
                })
        return books
    except FileNotFoundError :
        print("Books.txt not found, try creating a new file")
        return []

def save_books(books) :
    """To save books to books.txt"""
    with open('books.txt', 'w') as file:
        for book in books:
            file.write(f"{book['id']}, {book['title']}, {book['author']}, {book['total_copies']}, {book['available_copies']}\n")

def load_members() :
    """To load members from members.txt"""
    members = []
    try:
        with open('members.txt', 'r') as file :
            for line in file:
                member_data = line.strip().split(',')
                members.append({
                    'id': member_data[0].strip(),
                    'name': member_data[1].strip(),
                    'issued_book_ID': member_data[2].strip().split(';') if len(member_data) > 2 else []
                })
        return members
    except FileNotFoundError :
        print("members.txt not found, try creating a new file")
        return []

def save_members(members) :
    """To save members to members.txt"""
    with open('members.txt', 'w') as file:
        for member in members:
            issued_book_ID = ';'.join(member['issued_book_ID']) if member['issued_book_ID'] else ''
            file.write(f"{member['id']}, {member['name']}, {issued_book_ID}\n")

def view_books(books) :
    """To display all books in a format"""
    print("\n{:<10} {:<30} {:<20} {:<15} {:<15}".format("Book ID", "Title", "Author", "Total Copies", "Available"))
    print("-" * 90)
    for book in books:
        print("{:<10} {:<30} {:<20} {:<15} {:<15}".format(
            book['id'], book['title'], book['author'], 
            book['total_copies'], book['available_copies']
        ))

def binary_search_books(books, title) :
    """Binary search for a book by title"""
    sorted_books = sorted(books, key=lambda x: x['title'].lower())

    left, right = 0, len(sorted_books) - 1
    title = title.lower()

    while left <= right:
        mid = (left + right) // 2
        mid_title = sorted_books[mid]['title'].lower()

        if mid_title == title:
            return sorted_books[mid]
        elif mid_title < title:
            left = mid + 1
        else:
            right = mid - 1

    return None

def linear_search_books(books, title ) :
    """Linear search for a book by title"""
    title = title.lower()
    for book in books:
        if book['title'].lower() == title:
            return book
    return None

def issue_book(books, members, book_id, member_id) :
    """Issuing a book to a member"""
    # To find the book
    book = next((b for b in books if b['id'] == book_id), None)
    member = next((m for m in members if m['id'] == member_id), None)

    if not book or not member :
        print("Book or member not found.")
        return False

    # To check if the member has already issued 3 books
    if len(member['issued_book_ID']) >= 3 :
        print("Member has already issued 3 books. Cannot issue more.")
        return False

    # To check if the book is available
    if book['available_copies'] <= 0 :
        print("No copies of this book are available.")
        return False

    # To update book and member details
    book['available_copies'] -= 1
    member['issued_book_ID'].append(book_id)

    # To save updated data
    save_books(books)
    save_members(members)

    print(f"Book - {book_id} issued to member - {member_id}")
    return True

def return_book(books, members, book_id, member_id):
    """To return a book"""
    # To find the book
    book = next((b for b in books if b['id'] == book_id), None)
    member = next((m for m in members if m['id'] == member_id), None)

    if not book or not member :
        print("Book or member not found.")
        return False

    # To check if member has the book
    if book_id not in member['issued_book_ID']:
        print("Member did not issue this book.")
        return False

    # To update book and member details
    book['available_copies'] += 1
    member['issued_book_ID'].remove(book_id)

    # To save updated data
    save_books(books)
    save_members(members)

    print(f"Book - {book_id} returned by member - {member_id}")
    return True

def add_book(books) :
    """To add a new book to the system"""
    book_id = str(len(books) + 1)
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    total_copies = int(input("Enter total number of copies: "))

    new_book = {
        'id': book_id,
        'title': title,
        'author': author,
        'total_copies': total_copies,
        'available_copies': total_copies
    }

    books.append(new_book)
    save_books(books)
    print(f"Book - '{title}' added successfully with ID - {book_id}")

def view_members(members) :
    """To display all members and their issued books"""
    print("\n{:<10} {:<20} {:<30}".format("Member ID", "Name", "Issued Book IDs"))
    print("-" * 60)   
    for member in members:
        issued_books = ', '.join(member['issued_book_ID']) if member['issued_book_ID'] else ''
        print("{:<10} {:<20} {:<30}".format(
            member['id'], member['name'], issued_books
        ))

def register_member(members) :
    """To register a new member"""
    member_id = str(len(members) + 1)
    name = input("Enter member name: ")

    new_member = {
        'id': member_id,
        'name': name,
        'issued_book_ID': []
    }

    members.append(new_member)
    save_members(members)
    print(f"Member - '{name}' registered successfully with ID - {member_id}")
