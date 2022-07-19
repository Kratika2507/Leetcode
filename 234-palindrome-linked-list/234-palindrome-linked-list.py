# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        while head:
            i=head.val
            arr.append(i)
            head=head.next
        
        reverse= arr[::-1]
        
        if reverse==arr:
            return True
        else:
            return False
            
        