def oord(s): return ord(s)-ord("A")
def solve(s):
	l=list(s)
	a=[0 for i in range(26)]
	for i in l: a[oord(i)]+=1
	c=[0 for i in range(10)]
	c[0]=a[oord("Z")]
	c[2]=a[oord("W")]
	c[4]=a[oord("U")]
	c[6]=a[oord("X")]
	c[8]=a[oord("G")]
	for G in list("ERO"): a[oord(G)]-=a[oord("Z")]
	for G in list("TO"): a[oord(G)]-=a[oord("W")]
	for G in list("FOR"): a[oord(G)]-=a[oord("U")]
	for G in list("SI"): a[oord(G)]-=a[oord("X")]
	for G in list("EIHT"): a[oord(G)]-=a[oord("G")]
	c[3]=a[oord("H")]
	c[5]=a[oord("F")]
	for G in list("TREE"): a[oord(G)]-=a[oord("H")]
	for G in list("IVE"): a[oord(G)]-=a[oord("F")]
	c[1]=a[oord("O")]
	c[7]=a[oord("V")]
	c[9]=a[oord("I")]
	R=""
	for i in range(10): R+=str(i)*c[i]
	return R

testcase = input()
for i in range(testcase):
    print "Case #"+str(i+1)+":",
    print solve(raw_input())
