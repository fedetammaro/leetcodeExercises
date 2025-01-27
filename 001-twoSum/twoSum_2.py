class Solution():
    def twoSum(self, nums, target):
        seen = {}

        for index in range(0, len(nums)):
            difference = target - nums[index]

            if difference in seen:
                return seen[difference], index
            else:
                seen[nums[index]] = index


if __name__ == '__main__':
    test_nums = [3,3]
    test_target = 6

    solution = Solution()
    print(solution.twoSum(test_nums, test_target))