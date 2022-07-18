# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        
       
        dummy=[]
        while head:
            if head.next in dummy:
                return True
            else:
                dummy.append(head)
                head=head.next
        return False
            
            
        