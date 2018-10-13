def isIncreasing(num):
	num = str(num)
	length = len(num)

	for i in xrange(length-1):
		if num[i]>num[i+1]:
			return False

	return True

t = int(raw_input())

for i in xrange(t):

	num = int(raw_input())

	for j in xrange(num,0,-1):
		if isIncreasing(j)==True:
			ans = str(j)
			break


	print "Case #{}: {}".format(i+1, ans)


# if __name__=="__main__":
# 	print isIncreasing('1')
# 	print isIncreasing('22')
# 	print isIncreasing('999')
# 	print isIncreasing('9998')
# 	print isIncreasing('99381048')
# 	print isIncreasing('55')