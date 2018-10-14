import math

number_of_cases=int(input())

def scalar(f, x):
	return [f*t for t in x]

def mag(x):
	return math.sqrt(sum([t*t for t in x]))

def norm(x):
	m=mag(x)
	if m==0:
		return [0 for t in x]
	return [t/m for t in x]

def dot(x, y):
	return sum([a*b for a, b in zip(x,y)])

def sub(x, y):
	res=[0, 0, 0]
	for i in range(3):
		res[i]=x[i]-y[i]
	return res

def total(l):
	tot=[0, 0, 0]
	for item in l:
		for i in range(3):
			tot[i]+=item[i]
	return tot	

def average(l):
	tot=[0, 0, 0]
	tot=total(l)
	for i in range(3):
		tot[i]/=len(l)
	return tot


out=open("out.txt","w")

for case_n in range(number_of_cases):
	n=int(input())
	fly_coords=[]
	fly_veloc=[]
	for i in range(n):
		x, y, z, vx, vy, vz=map(int, input().split())
		fly_coords.append((x,y,z))
		fly_veloc.append((vx, vy, vz))
	#Find or
	a=init_center=average(fly_coords)
	b=veloc_moving=average(fly_veloc)
	
	#Find perpendicular
	project_mag=dot(a, norm(b))
	project=scalar(project_mag,norm(b))
		
	if project_mag>0 or mag(b)==0:
		d_min=mag(a)
		t_min=0.0
	else:
		perp=sub(a, project)
		d_min=mag(perp)		
		t_min=-project_mag/mag(b)
	
	out.write("Case #{0}: {1} {2}\n".format(case_n+1, d_min, t_min))