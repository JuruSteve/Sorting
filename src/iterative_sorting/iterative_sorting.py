# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    print('arr', arr, '\n')
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        print(f"cur_index: {cur_index}. smallest_index: {smallest_index}")
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for k in range(smallest_index, len(arr)):
            if arr[k] < arr[smallest_index]:
                smallest_index = k
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp
        # TO-DO: swap
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
