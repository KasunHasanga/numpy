from numpy import *

arr1 = array([1,2,3,4,5,6])
arr2 = array([6,5,4,3,3,5])
arr3 = arr2-+arr1

arr4=arr3.copy()
print(arr3)

print(id(arr1))
print(id(arr2))
print(id(arr3))
print(id(arr4), "arry 4")


