class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        temp=head
        while temp!=None:
            curr=temp.next
            temp.next=prev
            prev=temp
            temp=curr
        return prev