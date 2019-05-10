from numpy import *

arr1 = array([1,2,3,4,5,6])
arr2 = array([6,5,4,3,3,5])

arr3=arr1.copy()


arr3[3]=6
print(arr3)
print(arr1)
print(concatenate([arr1,arr3]))
print(id(arr1))
print(id(arr3))