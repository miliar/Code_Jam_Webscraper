import sys

def solution():
	string=["ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"]
	c=["our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"]
	
	mapper = dict()
	for ind in range(3):
		arr = list(c[ind])
		for i in range(len(arr)):
			if arr[i]!=" ":
				mapper[string[ind][i]] =  arr[i]
	mapper["z"] = "q"
	mapper["q"] = "z"

	testcase = int(sys.stdin.readline().strip())
	case =1
	for tc in range(testcase):
		str1 = sys.stdin.readline().strip()
		rs =""
		for i in str1:
			if i!=" ":
				rs+=mapper[i]
			else:
				rs+=" "
		print "Case #%d: %s"%(case,rs)
		case+=1
solution()
