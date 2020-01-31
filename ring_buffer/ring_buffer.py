from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail 
        else:
            if self.current.next is not None:
                self.current.next.value = item
                self.current = self.current.next
            else:
                self.storage.head.value = item
                self.current = self.storage.head

    def get(self):
        list_buffer_contents = []

        # TODO: Your code here
        cur_node = self.storage.head
        while cur_node is not None:
            if cur_node.value is not None:
                list_buffer_contents.append(cur_node.value)
            cur_node = cur_node.next

        return list_buffer_contents

# # ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
