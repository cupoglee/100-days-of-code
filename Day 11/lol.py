class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occur = {}
        l = len(nums)//2
        for num in nums:
            if num not in occur:
                occur[num]=0
            occur[num]+=1
            if occur[num]>l:
                return num
            else:
                pass