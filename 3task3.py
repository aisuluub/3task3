
def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
 
 
nums = [1, 2, 3, 4, 5, 6, 7]
print(nums)
 
shift(nums, -2)
print(nums)
 
shift(nums, 3)
print(nums)