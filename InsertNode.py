
class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
    
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
    
    # Method for inserting a new node at the start of a Linked List
    def insert_at_front(self,data):
        # make new node using data
        # set next pointer of new node to current head's next pointer
        # move head pointer to new node
        new_node = Node()
        new_node.data = data
        
        if self.head == None:
            head = new_node
    
        new_node.next = self.head
        self.head = new_node
