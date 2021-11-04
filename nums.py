def find_missing_nums(nums):
    flag = 0 # индикатор совпадения цифры
    memory = [] # список, в который мы будем записывать отсутсвующие цифру
    length = len(nums) # длина данного списка nums
    for i in range(1, length + 1):
        for j in range(0, length):
            if i == nums[j]:
                flag = 1
        if flag == 0:
            memory.append(i)
        flag = 0
    return memory
