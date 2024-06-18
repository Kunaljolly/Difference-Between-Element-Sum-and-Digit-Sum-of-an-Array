class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        t = 0
        for x in nums:
            for y in str(x):
                t += int(y)
                
        return sum(nums)-t
