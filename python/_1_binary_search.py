# Test array
list1 = [1, 2, 5, 7, 8, 12, 14, 16, 24]
list2 = [34, 1, 23, 47, 32, 2, 43, 7, 9]

# ---
# Selection sort
def slection_sort(arr):
    # 1. Find the smallest
    # 2. Insert the smallest el in new list
    # 3. Repeat until all elements are finished 
    def find_min(arr):
        minimal_el = arr[0]
        min_index = 0
        for i in range(len(arr)):
            if arr[i] < minimal_el:
                minimal_el = arr[i]
                min_index = i
        return min_index
    output = []
    for i in range(len(arr)):
        smallest = find_min(arr)
        output.append(arr.pop(smallest))
    return output


# ---
# Binary search
def binary_search(arr, el_to_find):
    # 1. Sort an array
    # 2. Find the middle
    # 3. ELement is higher or lower?
    # 4. Take the corresponding part and find the middle
    # 5. Go to the first step until you find the right one or the remainder will become less than zero.
    arr = slection_sort(arr)
    print("Отсортированный массив:", arr)

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
    

print("Найденный элемент (индекс в массиве): " + str(binary_search(list2, 47)))