#!/usr/bin/env python3
# Run with: python3 ExerciseSet2.py
from array import *
import time

def insertSort(arr):
    for x in range(1, len(arr)):
        num = arr[x]
        y = x-1
        while y >= 0 and num < arr[y]:
            arr[y+1] = arr[y]
            y -= 1
        arr[y+1] = num

# This code is contributed by Mayank Khanna (https://www.geeksforgeeks.org/merge-sort/)
# Python program for implementation of MergeSort
def mergeSort(arr, k):
    if len(arr) >k:
        mid = len(arr)//2 # Finding the mid of the array
        L = arr[:mid] # Dividing the array elements 
        R = arr[mid:] # into 2 halves
 
        mergeSort(L, k) # Sorting the first half
        mergeSort(R, k) # Sorting the second half
 
        i = j = k = 0
         
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1
         
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1
         
        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1
    else:
        insertSort(arr)


# Python program for implementation of Quicksort Sort
# This code is contributed by Mohit Kumra (https://www.geeksforgeeks.org/python-program-for-quicksort/)
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high, k):
    if len(arr) == 1:
        return arr
    elif len(arr) <= k:
        return insertSort(arr)
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1, k)
        quickSort(arr, pi+1, high, k)


# Radix sort in Python (https://www.programiz.com/dsa/radix-sort)
# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


# Python3 program to perform basic timSort (https://www.geeksforgeeks.org/timsort/)
MIN_MERGE = 32
  
def calcMinRun(n): 
    """Returns the minimum length of a  
    run from 23 - 64 so that 
    the len(array)/minrun is less than or  
    equal to a power of 2. 
  
    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,  
    ..., 127=>64, 128=>32, ... 
    """
    r = 0
    while n >= MIN_MERGE: 
        r |= n & 1
        n >>= 1
    return n + r 
  
  
# This function sorts array from left index to 
# to right index which is of size atmost RUN 
def insertionSort(arr, left, right): 
    for i in range(left + 1, right + 1): 
        j = i 
        while j > left and arr[j] < arr[j - 1]: 
            arr[j], arr[j - 1] = arr[j - 1], arr[j] 
            j -= 1
  
  
# Merge function merges the sorted runs 
def merge(arr, l, m, r): 
      
    # original array is broken in two parts 
    # left and right array 
    len1, len2 = m - l + 1, r - m 
    left, right = [], [] 
    for i in range(0, len1): 
        left.append(arr[l + i]) 
    for i in range(0, len2): 
        right.append(arr[m + 1 + i]) 
  
    i, j, k = 0, 0, l 
      
    # after comparing, we merge those two array 
    # in larger sub array 
    while i < len1 and j < len2: 
        if left[i] <= right[j]: 
            arr[k] = left[i] 
            i += 1
  
        else: 
            arr[k] = right[j] 
            j += 1
  
        k += 1
  
    # Copy remaining elements of left, if any 
    while i < len1: 
        arr[k] = left[i] 
        k += 1
        i += 1
  
    # Copy remaining element of right, if any 
    while j < len2: 
        arr[k] = right[j] 
        k += 1
        j += 1
  
  
# Iterative Timsort function to sort the 
# array[0...n-1] (similar to merge sort) 
def timSort(arr): 
    n = len(arr) 
    minRun = calcMinRun(n) 
      
    # Sort individual subarrays of size RUN 
    for start in range(0, n, minRun): 
        end = min(start + minRun - 1, n - 1) 
        insertionSort(arr, start, end) 
  
    # Start merging from size RUN (or 32). It will merge 
    # to form size 64, then 128, 256 and so on .... 
    size = minRun 
    while size < n: 
          
        # Pick starting point of left sub array. We 
        # are going to merge arr[left..left+size-1] 
        # and arr[left+size, left+2*size-1] 
        # After every merge, we increase left by 2*size 
        for left in range(0, n, 2 * size): 
  
            # Find ending point of left sub array 
            # mid+1 is starting point of right sub array 
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
  
            # Merge sub array arr[left.....mid] & 
            # arr[mid+1....right] 
            merge(arr, left, mid, right) 
  
        size = 2 * size 
 
# Code to print the list
def printList(arr):
    for i in range(len(arr)):        
        print(arr[i], end =" ")
    print()


f = open("RandomNumbers.txt", "r")
nums = [[], [], [], [], [], [], [], [], [], []]

for x in range(10):
    line = f.readline()[0:-2]
    nums[x] = [int(s) for s in line.split(' ')]

f.close()

print('Starting sorts')
f = open("Timings.txt", "w")
print('Merge sort k = 10')
avg = 0
for x in range(10):
    print(x)
    arr = nums[x].copy()
    start = time.time()
    mergeSort(arr, 10)
    end = time.time()
    f.write("Mergesort(k=10)[" + str(x) + "]: " + str(end-start) + " seconds\n")
    avg += (end-start)

f.write("Average: " + str(avg/10.0) + " seconds\n\n")
print('Merge sort k = 1000')
avg = 0
for x in range(10):
    print(x)
    arr = nums[x].copy()
    start = time.time()
    mergeSort(arr, 1000)
    end = time.time()
    f.write("Mergesort(k=1000)[" + str(x) + "]: " + str(end-start) + " seconds\n")
    avg += (end-start)

f.write("Average: " + str(avg/10.0) + " seconds\n\n")
print('Quick sort k = 10')
avg = 0
for x in range(10):
    print(x)
    arr = nums[x].copy()
    start = time.time()
    quickSort(arr, 0, len(arr)-1, 10)
    end = time.time()
    f.write("Quicksort(k=10)[" + str(x) + "]: " + str(end-start) + " seconds\n")
    avg += (end-start)

f.write("Average: " + str(avg/10.0) + " seconds\n\n")
print('Quick sort k = 1000')
avg = 0
for x in range(10):
    print(x)
    arr = nums[x].copy()
    start = time.time()
    quickSort(arr, 0, len(arr)-1, 1000)
    end = time.time()
    f.write("Quicksort(k=1000)[" + str(x) + "]: " + str(end-start) + " seconds\n")
    avg += (end-start)

f.write("Average: " + str(avg/10.0) + " seconds\n\n")
print('Radix sort')
avg = 0
for x in range(10):
    print(x)
    arr = nums[x].copy()
    start = time.time()
    radixSort(arr)
    end = time.time()
    f.write("Radix sort[" + str(x) + "]: " + str(end-start) + " seconds\n")
    avg += (end-start)

f.write("Average: " + str(avg/10.0) + " seconds\n\n")
print('Tim sort')
avg = 0
for x in range(10):
    print(x)
    arr = nums[x].copy()
    start = time.time()
    timSort(arr)
    end = time.time()
    f.write("Tim sort[" + str(x) + "]: " + str(end-start) + " seconds\n")
    avg += (end-start)

f.write("Average: " + str(avg/10.0) + " seconds\n\n")

f.close()
