fp=open("D-large.in","r")
ptr=open("output.txt","w")
num_cases=int(fp.readline())
for i in range(num_cases):
	tot_masses=int(fp.readline())
	masses1=fp.readline().split()
	naomi=map(float,masses1)
	masses2=fp.readline().split()
	ken=map(float,masses2)
	d_naomi=naomi[:]
	d_ken=ken[:]
	war,deceive_war=0,0
	ken.sort()
	for j in range(tot_masses):
		if max(ken)>naomi[j]:
			for k in ken:
				if k>naomi[j]:
					ken.remove(k)
					break
		else:
			ken.remove(min(ken))
			war+=1


		if min(d_naomi)<min(d_ken):
			d_naomi.remove(min(d_naomi))
			d_ken.remove(max(d_ken))
		else:
			d_naomi.remove(min(d_naomi))
			d_ken.remove(min(d_ken))
			deceive_war+=1
	ptr.write("Case #{}: {} {}\n".format(i+1,deceive_war,war))
