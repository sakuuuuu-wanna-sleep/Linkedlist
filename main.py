
import csv


def get_key(obj):
    return obj.title()


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self.num_of_nodes = 0

    def insert_at_start(self, data):
        new_node = Node(data) # create a new node with data

        if self.head_node is None: # if list is empty
            self.head_node = new_node # the new node is the head node
        else:
            new_node.next_node = self.head_node # the new nodemusr point to the
            self.head_node = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        self.num_of_nodes += 1
        if self.head_node is None: # if list is empty
            self.head_node = new_node# the new node is the head node
        else:
            temp_node = self.head_node
            while temp_node.next_node is not None:
                temp_node = temp_node.next_node

            temp_node.next_node = new_node

    def insert_after(self, data, previous_data):
        new_node = Node(data)
        self.num_of_nodes +=1
        if self.head_node is None:
            self.head_node = new_node
        else:
            temp_node = self.head_node
            while temp_node.data != previous_data and temp_node.next_node is not None:
                temp_node = temp_node.next_node
            new_node.next_node = temp_node.next_node
            temp_node.next_node = new_node

    def remove_item(self, data):
        self.num_of_nodes -= 1
        temp_node = self.head_node
        while temp_node.next_node.data != data and temp_node.next_node is not None:
            temp_node = temp_node.next_node
        if temp_node.next_node.next_node is None:
            temp_node.next_node = temp_node.next_node.next_node
            if temp_node == self.head_node:
                self.head_node = temp_node.next_node
        else:
            temp_node.next_node = None

    def add(self, data):
        new_node = Node(data)
        self.num_of_nodes += 1
        if self.head_node is None: # if list is empty
            self.head_node = new_node # the new node is the head node
        elif new_node.data.title < self.head_node.data.title:
            new_node.next_node = self.head_node
            new_node = self.head_node
        else:
            temp_node = self.head_node
            while temp_node.next_node is not None and temp_node.data.title < temp_node.next_node.data.title:
                temp_node = temp_node.next_node
            new_node.next_node = temp_node.next_node
            temp_node.next_node = new_node

    def __repr__(self):
        output = ""
        current_node = self.head_node
        while current_node is not None:
            output += current_node.__repr__() + "\n"
            current_node = current_node.next_node
        return output


class Book:
    list_of_books = LinkedList()

    def __init__(self, author, title, ISBN):
        self.author = author
        self.title = title
        self.ISBN = str(ISBN)
        Book.list_of_books.add(self)

    @classmethod
    def instantiate_from_csv(cls, filename: str):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
            print(items)
        for item in items:
            Book(
                author=item.get("Author"),
                title=item.get("Title"),
                ISBN=item.get("Primary ISBN10"),
            )

    def __repr__(self):
        return f"{self.title} by {self.author}"


if __name__ == '__main__':
    Book.instantiate_from_csv("Books.csv")
    print(Book.list_of_books)

