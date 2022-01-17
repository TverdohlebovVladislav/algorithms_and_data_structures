# Test array
list1 = [1, 2, 5, 7, 8, 12, 14, 16, 24]

# ---
# Binary search
def binary_search(arr, el_to_find):
    # 1. Find the middle
    # 2. ELement is higher or lower?
    # 3. Take the corresponding part and find the middle
    # 4. Go to the first step until you find the right one or the remainder will become less than zero.
    first = 0;
    last = len(arr) - 1

    while (first <= last):
        middle = (first + last) // 2
        if arr[middle] < el_to_find:
            first = middle + 1
        elif arr[middle] > el_to_find:
            last = middle - 1
        elif arr[middle] == el_to_find:
            return middle

    return "Элемент отсутствует!"
    

print("Найденный элемент (индекс в массиве): " + str(binary_search(list1, 5)))