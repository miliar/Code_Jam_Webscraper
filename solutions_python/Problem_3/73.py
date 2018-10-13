
import math

class point:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		
class square:
	def __init__(self,p4,l):
		self.p4=p4
		self.p1=point(p4.x-l,p4.y)
		self.p2=point(p4.x-l,p4.y+l)
		self.p3=point(p4.x,p4.y+l)
		self.l=l

def getRadius(p):
	return math.sqrt(p.x**2+p.y**2)

def getCutpoints(a_square,r):
	p1_Radius=getRadius(a_square.p1)
	p2_Radius=getRadius(a_square.p3)
	
	if p1_Radius<r:
		# CP1 non 'l2'
		x=a_square.p1.x
		y=math.sqrt(r**2-x**2)
		CP1=point(x,y)
	else:
		# CP1 non 'l1'
		y=a_square.p1.y
		x=-math.sqrt(r**2-y**2)
		CP1=point(x,y)
		
	if p2_Radius<r:
		# CP2 non 'l3'
		y=a_square.p3.y
		x=-math.sqrt(r**2-y**2)
		CP2=point(x,y)
	else:
		# CP2 non 'l4'
		x=a_square.p3.x
		y=math.sqrt(r**2-x**2)
		CP2=point(x,y)
	
	return CP1,CP2

def get_t1(CP1):
	degree=math.atan2(CP1.y,math.fabs(CP1.x))
	area=0.5*(CP1.y*math.fabs(CP1.x))
	return degree,area

def get_t2(CP2):
	degree=math.atan2(CP2.y,math.fabs(CP2.x))
	area=0.5*(CP2.y*math.fabs(CP2.x))
	return degree,area
	
def get_f1(t1_degree,t2_degree,r):
	return (t2_degree-t1_degree)*(r**2)/2.0
	
	
def get_r1(CP1,CP2,s_p4):
	r_p2=point(CP1.x,CP2.y)
	
	area=(math.fabs(s_p4.x-r_p2.x)*math.fabs(s_p4.y-r_p2.y))
	return area,r_p2
	
def calculate_area(f_square,r):
	CP1,CP2=getCutpoints(f_square,r)

	
	t1_degree,t1_area=get_t1(CP1)
	t2_degree,t2_area=get_t2(CP2)
	
	f1_area=get_f1(t1_degree,t2_degree,r)
	r1_area,r_p2=get_r1(CP1,CP2,f_square.p4)
	
	r2_area=(math.fabs(r_p2.x)*math.fabs(r_p2.y))
	
	outside_area=r2_area-t1_area-t2_area-f1_area

	
	a=r1_area-outside_area
	return a
	
	
def decide_intersection_area(a_square,r):

	
	if getRadius(a_square.p2)<r:
		return a_square.l**2
	elif getRadius(a_square.p4)>r:
		return None
	else:
		return calculate_area(a_square,r)




def scanRow(R,t,f,g,r,p2y):
	total=0.0
	x=-r
	while True:
		p=point(x-f,p2y+f)
		if g<2*f:
			return 0

		#print "p.x is",p.x,p.y
		fly_square=square(p,(g-2*f))
		circle_r=R-t-f
		a=decide_intersection_area(fly_square,circle_r)
		if a==None:
			break
		else:
			total+=a
		x-=(g+2*r)
	return total
	
def scanQuauter(R,t,f,g,r):
	total=0.0
	y=r
	while y<R-t:
		#print "y",y
		next_p2y=y
		row_total=scanRow(R,t,f,g,r,next_p2y)
		total+=row_total
		y+=(g+2*r)

	return total	


def calculateP(R,t,f,g,r):
	quarter=scanQuauter(R,t,f,g,r)
	
	return 1-quarter*4/(math.pi*(R**2))
	
def handleOneCase(input_f):
	parts=input_f.readline().split()

	f=float(parts[0])
	R=float(parts[1])
	t=float(parts[2])
	r=float(parts[3])
	g=float(parts[4])

	return calculateP(R,t,f,g,r)

def main_solve():
	import sys
	
	#sys.stdout=open("debug.output","w")
	
	input_f=open(sys.argv[1],"r")
	first_line=input_f.readline()
	case_num=int(first_line)
	result_f=open("result.output","w")
	
	for i in range(case_num):

		print "Case ",i+1
		sys.stdout.flush()
		result_f.write("Case #%d: "%(i+1))
		p=handleOneCase(input_f)
		result_f.write("%.6f\n"%p)
		i+=1
	
	
main_solve()