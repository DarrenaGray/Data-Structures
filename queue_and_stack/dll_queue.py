from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        return value

    def dequeue(self):
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.__len__()


q = Queue()
# print(q)
print(q.enqueue(2))
print(q.enqueue(6))
print(q.enqueue(8))
print(q.dequeue())
print(q.len())
