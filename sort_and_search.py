import numpy as np

def request_num(question):
    try:
        num = int(input(question))
        return num
    except ValueError as ve:
        print("enter valid integer")
    return request_quantity()

def selection_sort(array):
    n = len(array)
    for x in range(n):
        min = x
        for y in range(x + 1, n):
            if (array[y] < array[min]):
                min = y
        array[x], array[min] = array[min], array[x]
    return array

def binary_search(array, target, low, high):
    if (low > high):
        return -1

    mid = (low + high) // 2
    if (array[mid] == target):
        return mid
    elif (array[mid] < target):
        return binary_search(array, target, mid + 1, high)
    else:
        return binary_search(array, target, low, mid - 1)

def main():
    array = []
    num_items = request_num("how many items? ")
    x = 0
    while(x < num_items):
        try:
            array.append(int(input("item number " + str(x + 1) + ": ")))
        except:
            print("enter valid integer")
            x -= 1
        x += 1

    print("current array:\n" + str(array))

    array = selection_sort(array)

    print("sorted array:\n" + str(array))

    target_num = request_num("what number do you want to find? ")

    index = binary_search(array, target_num, 0, len(array) - 1)
    if (index == -1):
        print("number is not in the array")
    else:
        print(str(target_num) + " is at index " + str(index))

if __name__ == "__main__":
    main()
