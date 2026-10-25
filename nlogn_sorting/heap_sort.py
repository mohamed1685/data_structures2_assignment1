def maxHeapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, n, largest)


def buildMaxHeap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(arr, n, i)


def heapSort(arr):
    n = len(arr)
    buildMaxHeap(arr)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        maxHeapify(arr, i, 0)


if __name__ == "__main__":
    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    heapSort(arr)
    for val in arr:
        print(val, end=" ")
