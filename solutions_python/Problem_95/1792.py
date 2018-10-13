import sys
import string

fin = file('A-small-attempt0.in')
fout = file('out-small-0', 'w')
T = int(fin.readline())
case = 1

string1 = "a o z q our language is impossible to understand\nthere are twenty six factorial possibilities\nso it is okay if you want to just give up"
string2 = "y e q z ejp mysljylc kd kxveddknmc re jsicpdrysi\nrbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\nde kr kd eoya kw aej tysr re ujdr lkgc jv" 
map = {}

for i in range(string1.__len__()):
	map[string2[i]] = string1[i]

for line in fin:
	fout.write("Case #" + str(case) + ": ")
	for char in line:
		fout.write(map[char])
	case += 1
