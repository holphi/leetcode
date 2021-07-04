class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            j = i + 1
            while j<len(nums):
                if(nums[i]+nums[j]==target):
                    return [i, j]
                else:
                    j = j + 1
        else:
            return []

s = Solution()
print(s.twoSum([2,8,12,9], 17))