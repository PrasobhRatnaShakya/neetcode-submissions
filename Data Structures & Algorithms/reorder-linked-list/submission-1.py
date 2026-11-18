# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        #divide the link list into 2 parts from middle
        second = slow.next
        slow.next = None

        #reverse 2nd linked list
        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev

        #interweaving the nodes

        ptr1, ptr2 = head, second

        #while looping ptr2(second) cause it is always equal or shorter than ptr1(head)
        while ptr2:
            nxt1, nxt2 = ptr1.next, ptr2.next
            ptr1.next = ptr2
            ptr2.next = nxt1
            ptr1, ptr2 = nxt1, nxt2
