# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def merge(self, arr: List[int], min, mid, max):

        #build left list
        left = []
        i = 0
        while min + i < mid:
            left.append(arr[min + i])
            i+=1 
        
        #build right list
        right = []
        i = 0
        while (mid + 1 + i) < max:
            right.append(arr[mid + 1 + i])
            i+=1

        #sort
        l = 0; r = 0; i = min
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                arr[i] = left[l]
                l+=1
            else:
                arr[i] = right[r]
                r+=1
            i+=1

        while l < len(left):
            arr[i] = left[l]
            l+=1
            i+=1
        
        while r < len(right):
            arr[i] = right[r]
            r+=1
            i+=1
    
        return
        


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        arr = []

        #make into a list
        i = 0
        while i < len(lists):
            ptr = lists[i]
            while ptr != None:
                arr.append(ptr.val)
                ptr = ptr.next
            i+=1
        

        #mergeSorrt Function
        def mergeSort(arr, min, max):

            #base case
            if min > max:
                return

            mid = min + (max-min)//2
            mergeSort(arr, min, mid)
            mergeSort(arr, mid+1, max)

            merge(arr, min, mid, max)

            return
        
        max = len(arr) - 1
        mergeSort(arr, 0, max)

        return arr
        






