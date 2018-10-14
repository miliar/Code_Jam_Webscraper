import sys
import os


def func2(s):
  slen = len(s)
  index = 0

  while index < (slen - 1):
    if int(s[index + 1]) >= int(s[index]):
      index = index + 1
      continue
    else:
      if index == 0:
      	res = str(int(s[0])-1) + '9' * (slen - 1)
        return res.lstrip('0')
      else:
        # print "Break index : " , index
        temp = s[index]
        # print "break int: "  , temp
        l = range(index+1)
        l.reverse()
        startindex = 0
        for i in l:
          if s[i]==temp:
            startindex = i
          else:
            break
        # print "startindex: "  , startindex
        res = s[:startindex] + str(int(s[startindex])-1) + '9' * (slen - startindex - 1)
        # print "result : " , res
        return res.lstrip('0')
  return s.lstrip('0')

# def getlast(num):
# 	while num >= 1:
# 		if func2(str(num)):
# 			return num
# 		else:
# 			num = num - 1
# 			continue

no_of_cases = int(raw_input())
# print "Number of test cases: {0}".format(no_of_cases)

testcases = []
for n in range(no_of_cases):
	testcases.append(raw_input().strip())

for index , value  in enumerate(testcases):
	print "Case #{0}: {1}".format(index+1 , func2(value))




	