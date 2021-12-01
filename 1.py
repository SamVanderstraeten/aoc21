file = open("input/1.sam", "r")
lines = file.readlines()

# Part I + fill list for part II
nums = []
prev = -1
c = 0
for line in lines:
    num = int(line.strip())
    if prev != -1 and num > prev:
        c+=1
    prev = num
    nums.append(num)
print(c)


# Part II
c = 0
for n in range(0, len(nums)):
    if n+2 < len(nums):
        sw1 = sum(nums[n:n+3])
        sw2 = sum(nums[n+1:n+4])
        if sw2 > sw1:
            c+=1
print(c)