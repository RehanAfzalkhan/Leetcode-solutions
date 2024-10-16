class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = nums[::2]
        odd = nums[1::2]

        for i in range(len(even)):
            for j in range(len(even)-i-1):
                if even[j]> even[j+1]:
                    even[j],even[j+1]=even[j+1],even[j]
                    
        for i in range(len(odd)):
            for j in range(len(odd)-i-1):
                if odd[j]<odd[j+1]:
                    odd[j],odd[j+1]=odd[j+1],odd[j]

        result=[]
        even_index=0
        odd_index=0
        for i in range(len(nums)):
            if i%2==0:
                result.append(even[even_index])
                even_index+=1
            else:
                result.append(odd[odd_index])
                odd_index+=1
        return result        
