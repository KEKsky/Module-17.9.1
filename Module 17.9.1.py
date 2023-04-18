def merge(left, right):
    sort = []
    left_i = right_i = 0
    left_len, right_len = len(left), len(right)

    for _ in range(left_len + right_len):
        if left_i < left_len and right_i < right_len:
            if left[left_i] <= right[right_i]:
                sort.append(left[left_i])
                left_i += 1
            else:
                sort.append(right[right_i])
                right_i += 1
        elif left_i == left_len:
            sort.append(right[right_i])
            right_i += 1
        elif right_i == right_len:
            sort.append(left[left_i])
            left_i += 1

    return sort


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] < element and array[middle+1] >= element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


str_start = str(input('Введите последовательность: '))
ctrl_numb = int(input('Введите любое число: '))
list_numb = merge_sort(list(map(int, list(str_start.split()))))
print(list_numb)
if ctrl_numb <= list_numb[0]:
    print('Не существует элемента меньше введенного числа')
elif ctrl_numb >= list_numb[len(list_numb)-1]:
    print('Введенное число больше любого элемента последовательности')
else:
    print(binary_search(list_numb, ctrl_numb, 0, len(list_numb)-1))