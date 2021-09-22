'''
Problem : This code returns the index of element(P) in the array(a) if found, 
else returns the expected index where the element is supposed to be. 

Recursive Solution: 
	Time Complexity (Worst Case): 
		if element exists : O(log n)
		if doesn't exist : O(n)
	Space Complexity :
		Auxilary stack space : O(log n)

'''
def binary_search(array, start, end, target_value, length):
	if target_value < array[0]:
		return 0
	if target_value > array[length-1]:
		return length
	mid = round((start+end)/2)
	if a[mid] == target_value:
		return mid
	elif start == end:
		if a[start] > target_value:
			return start 
		temp = array[start]
		while(start < length and array[start] == temp):
			start+=1
		return start
	elif target_value < array[mid]:
		return binary_search(array, start, mid-1, target_value, length)
	else:
		return binary_search(array, mid+1, end, target_value, length)

def find_index(a, P):
	return binary_search(a, 0, len(a), P, len(a))

a = [1,1,5,8,14,25,123]
print('index : ', find_index(a, 123))
