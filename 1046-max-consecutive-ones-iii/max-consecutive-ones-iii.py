class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        zeros = 0
        result = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            # for every zero encountered, increase count of zeros

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            # if no. of zeros exceeds k, shift left (shrink) and reduce zeros count

            result = max(result, right - left + 1)

        return result