class Solution():
    def twoSum(self, nums, target):
        for first_index in range(0, len(nums)):
            for second_index in range(first_index + 1, len(nums)):
                if nums[first_index] + nums[second_index] == target:
                    return first_index, second_index


if __name__ == '__main__':
    test_nums = [2,15,11,7]
    test_target = 9

    solution = Solution()
    print(solution.twoSum(test_nums, test_target))