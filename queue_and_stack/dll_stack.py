from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def __str__(self):  # Human readable object
        return f"{self.storage} {self.size}"

    def push(self, value):
        self.storage.add_to_head(value)
        return value

    def pop(self):
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.__len__()


s = Stack()
print(s)
print(s.push(1))
print(s.push(6))
print(s.push(0))
# print(s.push(9))
# print(f"Length is {s.len()}")
print(f"{s.pop()} was popped off")
print(f"{s.pop()} was popped off")
print(f"Length is now {s.len()}")
