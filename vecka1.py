def linear_search_algorithm(lst, target):
    """Linear search algorithm"""
    for i in range(0, len(lst)):
        if target == lst[i]:
            return i
    return -1


def insertion_sort_algorithm(lst):
    """Insertion sort algorithm"""
    for i in range(2, len(lst)):
        key = i
        while lst[key - 1] > lst[key] and key > 0:
            lst[key - 1], lst[key] = lst[key], lst[key - 1]
            key -= 1


def binary_search_algorithm(lst, target):
    """The list must be sorted before using this algorithm"""
    begin_index = 0
    end_index = len(lst) - 1
    while begin_index <= end_index:
        middle_index = (begin_index + end_index) // 2
        if lst[middle_index] == target:
            return middle_index
        elif lst[middle_index] < target:
            begin_index = middle_index + 1
        else:
            begin_index = middle_index - 1
    return -1


lst = [2, 6, 5, 1, 3, 4]
print(lst)
result = linear_search_algorithm(lst, 3)
print(result)
sorted_list = insertion_sort_algorithm(lst)
print(lst)
result2 = binary_search_algorithm(lst, 6)
print(result2)