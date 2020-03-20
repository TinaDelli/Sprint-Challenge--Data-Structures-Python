from doubly_linked_list import DoublyLinkedList

# A ring buffer is a non-growable buffer with a fixed size. 
# When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. 
# This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

# Implement this behavior in the RingBuffer class. 
# RingBuffer has two methods, append and get. 
# The append method adds elements to the buffer. 
# The get method, which is provided, returns all of the elements in the buffer in a list in their given order. 
# It should not return any None values in the list even if they are present in the ring buffer.

# You may not use a Python List in your implementation of the append method (except for the stretch goal)
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current is None: #add the first item and set to the current oldest item
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            return 
        if len(self.storage) >= self.capacity:
            if self.current is not self.storage.tail: #change to next and update it's value
                self.current.next.value = item
                self.current = self.current.next
            else: #change to head and update value
                self.current = self.storage.head
                self.current.value = item
        else: #if not at capacity add to tail and set current to updated next 
            self.storage.add_to_tail(item)
            self.current = self.current.next
            

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        head = self.storage.head
        while head:
            list_buffer_contents.append(head.value) #append value to buffer contents
            head = head.next #go to next node


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
