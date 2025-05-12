class Listnode:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next

def create_ll(arr):
    if not arr:
        return None
    head = Listnode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Listnode(val)
        current = current.next
    current = head
    while(current):
        print(current.data)
        current = current.next
    return head

head = create_ll([1,2,3,4,5,6])
