class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_pos(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 1

            while current and count < position:
                current = current.next
                count += 1

            if not current:
                raise IndexError("Position out of range")

            new_node.next = current.next
            current.next = new_node

    def delete_at_position(self, position):
        if not self.head:
            raise IndexError("List is empty")

        if position == 0:
            self.head = self.head.next
        else:
            current = self.head
            count = 1

            while current and count < position:
                current = current.next
                count += 1

            if not current or not current.next:
                raise IndexError("Position out of range")

            current.next = current.next.next

    def delete_after_node(self, node):
        if not node or not node.next:
            raise ValueError("Invalid node or no node after it")

        node.next = node.next.next

    def search_node(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True
            current = current.next

        return False


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def push(self, data):
        self.linked_list.insert_at_pos(data, 0)

    def pop(self):
        if not self.linked_list.head:
            raise IndexError("Stack is empty")

        data = self.linked_list.head.data
        self.linked_list.delete_at_position(0)
        return data

    def peek(self):
        if not self.linked_list.head:
            raise IndexError("Stack is empty")

        return self.linked_list.head.data


linked_list = LinkedList()
linked_list.insert_at_pos(1, 0)  
linked_list.insert_at_pos(9, 1)   

current = linked_list.head
while current:
    print(current.data)
    current = current.next