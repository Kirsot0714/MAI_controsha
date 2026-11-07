import random


def quick_sort(_list):
    l_s = len(_list)
    if l_s <= 1:
        return _list
    middle = l_s // 2
    middle_elem = _list[middle]
    left_part = []
    right_part = []
    middle_part = []
    for e in _list:
        if e < middle_elem:
            left_part.append(e)
        elif e > middle_elem:
            right_part.append(e)
        else:
            middle_part.append(e)
    return quick_sort(left_part) + middle_part + quick_sort(right_part)


test = [random.randint(1, 10) for i in range(10)]
print(test)
print(quick_sort(test))
