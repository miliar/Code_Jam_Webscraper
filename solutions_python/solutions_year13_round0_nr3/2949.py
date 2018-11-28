import math

import time

start = time.time()
def  num_list(num):
    a = str(num)
    if a == a[::-1]:
		new=int(math.sqrt(int(a)))
		if int(a) == new**2:
			new=str(new)
			if new == new[::-1]:
				flist.append(a)

FILE = open('C:\Users\IBM_ADMIN\Downloads\C-small-attempt0.in', 'r')
cnt = FILE.readline()
k = 1
for i in FILE:
    mm = i
    n = map(int, mm.split())[0]
    m = map(int, mm.split())[1]
    flist = []
    for i in range(int(n), int(m)+1):
        num_list(i)
    print "Case #" + str(k) + ": " + str(len(flist))
    k = k + 1

end = time.time()

print end-start


