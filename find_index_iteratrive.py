'''
Problem : This code returns the index of element(P) in the array(a) if found, 
else returns the expected index where the element is supposed to be. 

Iterative Solution: 
	Time Complexity (Worst Case): 
		if element exists : O(log n)
		if doesn't exist : O(n)
	Space Complexity : O(1)

'''
def find_index(a, P):
	length = len(a)
	start = 0
	end = length-1
	if P < a[0]:
		return 0
	if P > a[length-1]:
		return length
	while(start <= end):	#binary search
		mid = (start+end)//2
		if P < a[mid]:
			end = mid-1
		elif P > a[mid]:
			start = mid+1
		else:
			return mid
	if a[start] > P:
		return start 
	temp = a[start]
	while(start < length and a[start] == temp):
		start+=1
	return start		

a = [1,1,1,1,1,3,3,3,14]
print('index : ', find_index(a, 4))