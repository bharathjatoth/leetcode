# Problem: Given an array of integers and a target, return indices of the two numbers that add up to the target.
# nums = [2, 7, 11, 15], target = 9 → Output: [0, 1]
def sum(nums,target):
    x = {}
    for i,num in enumerate(nums):
        if target - num in x:
            return [i,x[target-num]]
        else:
            x[num] = i
    print(x)

print(sum([5,6,7,1,3,102],105))