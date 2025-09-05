def search(my_list, n):
    l = 0
    u = len(my_list)-1
    while l <= u:
        mid = (l+u) // 2
        if my_list[mid] == n:
            return mid
        elif n > my_list[mid]:
            l = mid + 1
        else:
            u = mid - 1
    return False






numbers = [x for x in range(15, 85, 3)]
n = int(input("Enter number to search: "))
index = search(numbers, n)

if index is not False:
    print("Found at index:", index)
else:
    print("Not found")