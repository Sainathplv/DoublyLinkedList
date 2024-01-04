class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def swap_first_last(self):
        if self.length <= 1:
            return  # No swap needed for empty or single-element list

        # If the list has only two elements
        if self.length == 2:
            self.head, self.tail = self.tail, self.head
            self.head.next = self.tail
            self.tail.prev = self.head
            self.head.prev = None
            self.tail.next = None
            return

        # Swap for list with more than two elements
        first_node = self.head
        last_node = self.tail

        # Adjusting the nodes next to the head and tail
        second_node = first_node.next
        second_last_node = last_node.prev

        # Swapping first and last nodes
        second_node.prev = last_node
        second_last_node.next = first_node

        # Adjusting head and tail
        self.head, self.tail = last_node, first_node
        self.head.next = second_node
        self.tail.prev = second_last_node

        # Setting correct next and prev for new head and tail
        self.head.prev = None
        self.tail.next = None


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)

print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.swap_first_last()

print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()
