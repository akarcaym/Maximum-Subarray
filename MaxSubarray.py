"""Yasin Yağız Gülten - 041501037
   Melis Akarçay - 041401015"""

import random
import math

arr1 = [-2, -5, 6, -2, -3, 1, 5, -6]
arr3 = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
size_arr1 = len(arr1)
size_arr3 = len(arr3)


def find_max_subarray(arr, size):             #run time n2
    left = 0
    right = 0
    max = arr[0]
    curSum = 0
    for i in range(size): # Increment left end of subarray
        curSum = 0
        for j in range(i, size): # Increment right end of subarray
            curSum = curSum + arr[j]
            if curSum > max:
                max = curSum
                left = i
                right = j
                subarray = arr[left:(right+1)]

    #return (left, right, max)

    print('The max subarray summation is(n2):' , max)

    for k in range(len(subarray)):
        print(subarray[k])

print("\n")
find_max_subarray(arr1, size_arr1)
find_max_subarray(arr3, size_arr3)

def maxCrossing(arr, low, m, high):              #run time nlogn (divide and conquer)
    max_sum = 0
    sum_left = -10000
    i = m
    while i > low-1:
        max_sum = max_sum + arr[i]
        if max_sum > sum_left:
            sum_left = max_sum
        i = i-1

    max_sum = 0
    sum_right = -10000
    i = m+1
    while i < high+1:
        max_sum = max_sum + arr[i]
        if max_sum > sum_right:
            sum_right = max_sum
        i = i+1

    return sum_left + sum_right

def maxSumSubarray(arr, low, high):             #run time nlogn (divide and conquer)
    if low == high:
        return arr[0]

    med = (low + high)//2

    return max(maxSumSubarray(arr, low, med), maxSumSubarray(arr, med+1, high), maxCrossing(arr, low, med, high))

print("\n")
nlogn_max_arr1 = maxSumSubarray(arr1, 0, size_arr1-1)
print("Max(nlogn) of arr1 is:", nlogn_max_arr1)
nlogn_max_arr3 = maxSumSubarray(arr3, 0, size_arr3-1)
print("Max(nlogn) of arr3 is:", nlogn_max_arr3)

def find_max_subarray_run_time_n(arr, size):  #runtime n
    max_value = arr[0]
    temp_max = arr[0]
    for i in range(1, size):
        temp_max = max(arr[i], temp_max + arr[i])
        if temp_max > max_value:
            max_value = temp_max

    return max_value


print("\n")
n_max_arr1 = find_max_subarray_run_time_n(arr1, size_arr1)
print("Max(n) of arr1 is:", n_max_arr1)
n_max_arr3 = find_max_subarray_run_time_n(arr3, size_arr3)
print("Max(n) of arr3 is:", n_max_arr3)
