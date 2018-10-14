from math import factorial as fac

f=open("input.txt","r")
lines=int(f.readline())
# print "lines: %d" %lines
case=0
out=open("output.txt","w")

for i in range(lines):
	d={}
	nums=f.readline().split()
	# print nums
	for j in range(int(nums[0]),int(nums[1])+1):
		td=[]
		temp=str(j)
		for k in range(1,len(temp)+1):
			td.append(temp[-k:]+temp[:len(temp)-k])
		d[j]=sorted(td)
		# print d[j]
	va=d.values()
	exclude=[]
	c=0
	for x in d:
		if d[x] in exclude:
			# print x,
			continue
		co=va.count(d[x])
		if co==1: continue
		exclude.append(d[x])
		# print co
		if co==2:c+=1
		elif co>2:
			# print co
			fa=fac(co)/(2*fac(co-2))
			# print fa
			c+=fa
		# print x,
	# print d
	# print c
	case+=1
	o="Case #%d: " %case
	out.write(o+str(c)+"\n")
f.close()
out.close()

raw_input()