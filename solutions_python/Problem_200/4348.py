#!/usr/bin/python

f = open("./case.txt", 'r')
w = open("./out.txt", 'w')
test_num = int(f.readline())
i = 0
while i<test_num:
	case_num = int(f.readline())
	flag = True
	while flag:
		if len(str(case_num)) == 1:
			flag = False
		else:
			checker = True
			prev = str(case_num)[0]
			for a in str(case_num)[1:]:
				if int(a) < int(prev):
					checker = False
					break
				else:
					prev = a
			if checker:
				flag = False
			else:
				case_num = case_num-1
	i = i+1
	res = 'Case #'+str(i)+': '+str(case_num)+'\n'
	w.write(res)
w.close()
f.close()
