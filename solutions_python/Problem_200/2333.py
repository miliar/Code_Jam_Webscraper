baca = open("B-large.in","r")
tulis = open("output.txt","w")
lst = []
def buat(s,n):
	if (n != 0) : lst.append(int(s))
	if (n == 19) : return 0
	if (len(s) != 0) : c = int(s[-1])
	else : c = 1
	for i in range(c,9+1):
		buat(s+str(i),n+1)
buat("",0)
lst.sort()
#print(lst)
#print(len(lst))
n = int(baca.readline())
for i in range(n):
	m = int(baca.readline())
	l = 0
	r = len(lst)
	while (l < r):
		mid = (l+r)//2
		if (lst[mid] == m) : break
		if (lst[mid] < m and m < lst[mid+1]) : break
		if (lst[mid] < m) : l = mid
		else : r = mid
	tulis.write("Case #"+str(i+1)+": "+str(lst[mid])+"\n")
		