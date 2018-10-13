def read_file(flname):
    with open(flname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def write_file(flname, content):
    with open(flname, 'a') as f:
        f.write(content+'\n')    
        

def is_tidy(n):
	lst = []
	m = str(n)
	for c in m:
		lst.append(int(c))
	lst.sort()
	o = ""
	for s in lst:
		o+=str(s)
	if o == m:
		return True
	return False

file_r = "B-small-attempt0.in"
file_w = "out.txt"
	
content = read_file(file_r)
T = int(content[0])
for i in xrange(T):
	tidy = 0
	num = long(content[i+1])
	tst = str(num)
	print(tst)
	for k in xrange(len(tst)-1):
		#print(k, tst[k], tst[k+1])
		if tst[k] > tst[k+1]:
			tst = tst[:k+1]+"0"*(len(tst)-(k)-1)
			#print(tst)
	for k in xrange(len(tst),1,-1):
		print(k, tst[k-1], tst[k-2])
		if tst[k-1]=="0" and tst[k-2]=="1" and k-2>0:
			tst = tst[:k-2]+"0"*(len(tst)-(k-2))
			print(tst)
	print(tst)
	num = int(tst)
	while num > 0:
		if is_tidy(num):
			tidy = num
			break
		num -= 1
	write_file(file_w, "Case #"+str(i+1)+": "+str(tidy))