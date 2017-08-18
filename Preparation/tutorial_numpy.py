import numpy as np

a = np.array([[1,2,3,4],[4,2,4,5]])
print(a[:2,:2])

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print(x+y)
print(np.add(x,y))


print(x-y)
print(np.subtract(x,y))

print(x*y)
print(np.multiply(x,y))

print(x/y)
print(np.divide(x,y))

print(np.sqrt(x))


v = np.array([9,10])
w = np.array([11,12])

print(x.dot(v))
print(np.dot(x,v))


print(x.dot(y))
print(np.dot(x,y))



print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))

b = np.empty_like(x)


for i in range(2):
	b[i, :] = x[i, :] + v

print(b)