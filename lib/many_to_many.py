class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        """Returns a list of contracts associated with the author."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Returns a list of books associated with the author through contracts."""
        return list(set(contract.book for contract in self.contracts()))

    def sign_contract(self, book, date, royalties):
        """Creates a new contract for the author and a book."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Calculates the sum of royalties from all contracts."""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        """Returns a list of contracts associated with the book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Returns a list of authors who have signed contracts for the book."""
        return list(set(contract.author for contract in self.contracts()))


class Contract:
    all = []  # Stores all contract instances

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Returns a list of contracts sorted by date, filtered by the given date."""
        return sorted([contract for contract in cls.all if contract.date == date], key=lambda c: c.date)
