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
    
    def twoSum_hash(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        
        for i in range(len(nums)):
            t = target - nums[i]
            if t in d.keys():
                return [i ,d[t]]
        else:
            return []

s = Solution()

print(s.twoSum([2,8,12,9], 17))
print(s.twoSum_hash([2,8,12,9], 17))