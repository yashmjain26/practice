def solution(lst, target):
    length = len(lst)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if lst[i] + lst[j] == target:
                new_list = i, j
                return tuple(new_list)
    return -1


list = [5, 6, 7, 8, 9, 10]
target = 15
print(solution(list, target))
