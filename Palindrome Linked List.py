class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow=head
        fast=head
        while fast.next!=None and fast.next.next!=None:
            fast=fast.next.next
            slow=slow.next
        slow.next=self.reverse(slow.next)
        temp=head
        curr=slow.next
        while curr!=None:
            if temp.val!=curr.val:
                return False
            temp=temp.next
            curr=curr.next
        return True
    def reverse(self,node):
        prev=None
        while node!=None:
            curr=node.next
            node.next=prev
            prev=node
            node=curr
        return prev