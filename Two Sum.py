#Given an array of integers,
#return indices of the two numbers
#such that they add up to a specific target.

#You may assume that each input would have
#exactly one solution, and you may not use
#the same element twice.
# Eg - [2,7,5,10](9), [3,2,4](6)

class Solution(object):
    def twoSum(self, nums, target):
        dict1 = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] not in dict1:
                dict1[diff] = i
            else:
                return [dict1[nums[i]], i]