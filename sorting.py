#Fahril Antonio Hande_F55123031
# #BubbleSort(arr):
#     n = length(arr)
#     for i from 0 to n-1:
#         for j from 0 to n-i-2:
#             if arr[j] > arr[j+1]:
#                 Swap arr[j] and arr[j+1]
# MergeSort(arr):
#     if length(arr) <= 1:
#         return arr
#     mid = length(arr) / 2
#     left = MergeSort(arr[0:mid])
#     right = MergeSort(arr[mid:length(arr)])
#     return Merge(left, right)

# Merge(left, right):
#     result = []
#     while left is not empty and right is not empty:
#         if left[0] <= right[0]:
#             Append left[0] to result
#             Remove left[0] from left
#         else:
#             Append right[0] to result
#             Remove right[0] from right
#     Append all remaining elements of left (if any) to result
#     Append all remaining elements of right (if any) to result
#     return result


# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Contoh penggunaan
if __name__ == "__main__":
    data1 = [64, 34, 25, 12, 22, 11, 90]
    data2 = [64, 34, 25, 12, 22, 11, 90]
    
    print("Array sebelum Bubble Sort:", data1)
    bubble_sort(data1)
    print("Array setelah Bubble Sort :", data1)
    
    print("\nArray sebelum Merge Sort:", data2)
    sorted_data = merge_sort(data2)
    print("Array setelah Merge Sort :", sorted_data)
