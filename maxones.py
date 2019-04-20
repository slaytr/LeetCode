#problem 485
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0 or i == len(nums)-1:
                if count > max_count:
                    max_count = count
                count = 0
        return max_count