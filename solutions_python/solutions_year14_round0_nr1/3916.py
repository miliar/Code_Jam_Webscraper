def case(i):
	mat1=[]
	q1=int(raw_input())
	for j in range(4):
		mat1.append([int(x) for x in raw_input().split()])
	# for i in range(4):
	# 	print mat1[i]
	q2 = int(raw_input())
	mat2=[]
	for j in range(4):
		mat2.append([int(x) for x in raw_input().split()])
	# for i in range(4):
	# 	print mat2[i]
	# print set(mat1[q1-1])
	# print set(mat2[q2-1])
	result = set(mat1[q1-1]).intersection(set(mat2[q2-1]))
	if len(result)==0:
		print "Case #%d: Volunteer cheated!"%i
		return
	if len(result)==1:
		print "Case #%d: %d"%(i, result.pop())
		return
	if len(result)>1:
		print "Case #%d: Bad magician!"%i
		return

def main():
	n = int(raw_input())
	for i in range(n):
		# print i
		case(i+1)

main()