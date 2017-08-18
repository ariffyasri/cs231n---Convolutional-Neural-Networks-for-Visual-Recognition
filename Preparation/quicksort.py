# source : http://cs231n.github.io/python-numpy-tutorial/

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	
	# the 'magic' is here :)
	return quicksort(left) + middle + quicksort(right)

print(quicksort([3,2,11,1,20,6,5,3,0]))