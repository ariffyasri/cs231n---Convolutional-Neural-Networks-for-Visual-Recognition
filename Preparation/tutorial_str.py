s = 'hello'
print(s.capitalize())
print(s.upper())
print(s.rjust(7))
print(s.center(7))
print(s.replace('l','(ell)'))
print(' word '.strip())


# dictionary comprehensions

nums = [0,1,2,3,4]
even_num = {x:x**2 for x in nums if (x%2) == 0}
print(even_num)


# tutorial numpy

# array

import numpy as np

a = np.array([1,2,3])
print(type(a))

print(a.shape)
print(a[0],a[1],a[2])
a[0] = 5
print(a)

b = np.array([[1,2,3], [4,5,6]])
print(b.shape)
print(b[0,0], b[1,1], b[1,2])


# create an array for all zeros

a = np.zeros((2,2))
print(a)

b = np.ones((1,2))
print(b)

c = np.full((2,2),7)
print(c)

d = np.eye(2)
print(d)

e = np.random.random((2,2))
print(e)



# array indexing

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

# slicing

b = a[:2,:1]

print(a[0,1])
a[0,0] = 777
print(a[0,1])