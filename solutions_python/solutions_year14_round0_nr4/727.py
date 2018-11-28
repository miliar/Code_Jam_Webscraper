import sys
import copy

tc = int(sys.stdin.readline())
dw = 0
def find_lowest_greater_than(seq,val):
	seq.sort()
	for i in range(len(seq)):
		if(seq[i] > val):
			return i
	return None

# def remove_higher_using_my_lower(n,k):
# 	dw_flag = True
# 	while dw_flag:
# 		if(n==[] or k==[]):
# 			dw_flag = False
# 			break
# 		if(n[0] < k[0]):
# 			k.pop()
# 			n.remove(n[0])
# 		else:
# 			dw_flag = False
# 	return n,k

# def win_with_my_highs(n,k):
# 	global dw
# 	dw_flag = True
# 	while dw_flag:
# 		if(n==[] or k ==[]):
# 			dw_flag = False
# 			break
# 		if( n[len(n)-1] < k[len(k)-1] ):
# 			n,k = remove_higher_using_my_lower(n,k)
# 		else:
# 			n.pop()
# 			k.remove(k[0])
# 			dw += 1
# 	return n,k

for t in range(1,tc+1):
	result_str = "Case #" + str(t) + ": "
	#logic here
	no_of_weight = int(sys.stdin.readline())
	naomi = sys.stdin.readline().strip().split()
	naomi = map(float,naomi)
	ken = sys.stdin.readline().strip().split()
	ken = map(float,ken)

	n = copy.deepcopy(naomi)
	k = copy.deepcopy(ken)
	n.sort()
	k.sort()


	#for deci war
	#dw = 0

	dw = 0 
	dw_flag = True
	while  dw_flag:
		if(n ==[] or k==[]):
			dw_flag = False
			break
		if (n[len(n)-1] < k[len(k)-1]):
			n.remove(n[0])
			k.pop()
		else:
			dw_flag = False
	dw_flag = True
	while dw_flag:
		if(n==[] or k==[]):
			dw_flag = True
			break
		if not(find_lowest_greater_than(n,k[0]) == None):
			n_index = find_lowest_greater_than(n,k[0])
			n.remove(n[n_index])
			k.remove(k[0])
			dw += 1
		else:
			dw_flag = False
	
	# n,k = remove_higher_using_my_lower(n,k)
	# dw =  len(n)
	#n, k = win_with_my_highs(n,k)
	# #n.reverse()
	# dw_flag = True
	# #print n
	# while dw_flag:
	# 	if(n==[] or k==[]):
	# 		dw_flag = False
	# 		break
	# 	if(k[len(k)-1] > n[len(n)-1]):
	# 		n.remove(n[0])
	# 		k.pop()
	# 	else:
	# 		dw_flag = False
	# #print n,k
	# dw_flag = True
	# while dw_flag:
	# 	if (n==[] or k==[]):
	# 		dw_flag = False
	# 		break
	# 	if(n[0]<k[0]):
	# 		#assert False
	# 		k.remove(k[0])
	# 		n.remove(n[0])
	# 	else:
	# 		dw_flag = False
	# #print n,k
	# if(n):
	# 	dw = len(n)

	result_str += str(dw) + " "

	# for war game
	w = 0
	n = copy.deepcopy(naomi)
	n.sort()
	n.reverse()
	k = copy.deepcopy(ken)
	k.sort()

	for n_value in n:
		if (k==[]):
			break
		if(n_value > k[len(k)-1]):
			against = k[0]
			k.remove(k[0])
		else:
			against = k.pop()
		if(n_value > against):
			w +=1
	result_str += str(w)

	print result_str