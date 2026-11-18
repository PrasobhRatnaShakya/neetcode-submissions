# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        curr = new_head = head
        count = 1

        while curr.next:
            curr = curr.next
            count += 1
        
        k = k%count
        idx = count - k

        if k == 0:
            return head 

        curr.next = head

        for _ in range(idx - 1):
            new_head = new_head.next
        
        tail = new_head
        new_head = new_head.next
        tail.next = None

        return new_head




        