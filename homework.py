# Problem 1: Add a .remove method to the LinkedList
#
# Update the .remove method to the LinkedList class to remove a node from the list.
#
# The method should take in the value to remove and remove the node with that value from the LinkedList.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<Node|{self.value}>"


class LinkedList:
    def __init__(self, head_node=None):
        self.head = head_node

    def push_on(self, new_value):
        # Add a new node with the given value to the beginning of the linked list
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def traverse_list(self):
        # traverse the linked list and print each node's value
        node = self.head
        while node is not None:
            print(node)
            node = node.next

    def append(self, new_value):
        # add a new node with the given value to the end of the linked list
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node

    def get_node(self, value_to_get):
        # find and return the node with the given value.
        node_to_check = self.head
        while node_to_check is not None:
            if node_to_check.value == value_to_get:
                return node_to_check
            node_to_check = node_to_check.next
        return None

    def insert_after(self, prev_value, new_value):
        # Insert a new node with the given value after the node with the previous value.
        prev_node = self.get_node(prev_value)
        if prev_node is None:
            print(f"{prev_value} is not in the linked list.")
        else:
            new_node = Node(new_value)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def find_before(self, value_to_get):
        # find and return the node before the node with the given value.
        node = self.head
        while node.next is not None:
            if node.next.value == value_to_get:
                return node
            node = node.next
        return None

    def remove(self, value_to_remove):

        # if the head node has the value to remove, set the next node as the new head
        if self.head.value == value_to_remove:
            self.head = self.head.next

        prev_node = self.head
        current_node = self.head.next

        # traverse the linked list to find the node with the value to remove
        while current_node is not None:
            if current_node.value == value_to_remove:
                prev_node.next = current_node.next
            prev_node = current_node
            current_node = current_node.next


# usage
weekdays = LinkedList()
list_of_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for day in list_of_days:
    weekdays.append(day)

# remove 'Tuesday' day from the list
weekdays.remove('Tuesday')

# print the updated list
weekdays.traverse_list()
