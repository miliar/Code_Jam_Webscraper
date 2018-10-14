import sys
sys.setrecursionlimit(100000)

def relieve(n,m):
	#print (n,m)
	max_space = max(n)
	max_position = n.index(max_space)
	#print(max_position,max_space)

	new_right = max_space//2
	new_left = max_space - new_right
	new_left -= 1
	
	n[max_position] = new_left
	n.insert(max_position+1,new_right)

	m -= 1

	#print(n,m)
	if m == 0:
		return new_left,new_right
	else:
		return relieve(n,m)


t = int(input())
for i in range(1, t + 1):
	n,m = [str(s) for s in input().split(" ")]
	result1,result2 = relieve([int(n)],int(m))
	print("Case #{}: {} {}".format( i,max([result1,result2]),min([result1,result2]) ))
