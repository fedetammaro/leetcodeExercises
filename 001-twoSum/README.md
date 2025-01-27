# Two sum
The very first exercise Leetcode has to offer, but still challenges you to improve your very first solution!

`Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to 
target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You 
can return the answer in any order.`

My immediate solution was to iterate through the array of given numbers, maintaining two separate indexes, one starting 
from 0 and the other starting from the previous index and going up. Comparing the sum of the two numbers with the target
and then returning the indexes when there is a hit. Simple enough!

`Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?`

Here's the (not so unexpected) twist! Given the obvious solution, they ask to optimize the time complexity. And from
previous experiences, if they ask to only optimize the time, some space must be used to not iterate through the list a
second time.

Given that I have to return the index of a number seen through the array, I need to somehow store the numbers I've 
already seen and their corresponding index in the array... So, a dictionary it is! Searching for a key has a O(1) time 
complexity, so I only need to iterate the array once to see every number and check whether the difference between the
target and the current number is present in the dictionary.

[Here is the submission](https://leetcode.com/problems/two-sum/submissions/1521914962)

Runtime 0ms - Beats 100.00%

Memory 13.26MB - Beats 37.23%