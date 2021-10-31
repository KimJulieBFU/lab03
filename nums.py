def find_missing_nums(nums):
    n = len(nums)
    s = []
    b = False
    for i in range (1,n+1):
        for j in range (0,n):
            if i == nums[j]:
                b = True
                continue
        if not b:
            s.append(i)
        b = False
    return s
