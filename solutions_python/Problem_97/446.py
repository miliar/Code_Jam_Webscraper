import sys

def recycled_numbers(a,b) :
	d={}
	l=10
	r=1
	k=a
	count = 0
	repeat = False

	while (k/10) > 0 :
		count = count + 1
		r = r * 10
		k=k/10
	
	for i in range(count) :
		x=a
		n2=b/r
		while x <= b :
			k=x%l
			if k <= n2 :
				y=k*r+x/l
				if x!=y and y>=a and y <= b :
					if x < y :
						p=x
						q=y
					else :
						p=y
						q=x
					if d.has_key(p) :
						d[p][q]=0
					else :
						d[p]={q:0}
				x=x+1
			else :
				x=x-(x%l)+l
		l=l*10
		r=r/10

	result = 0
	for key in d.keys() :
		result = result + len(d[key].keys())

	return result
		
if __name__ == "__main__" :
	t = int(raw_input())

	for i in range(t) :
		(a,b)=str(raw_input()).split(" ")
		sys.stdout.write("Case #"+str(i+1)+": "+str(recycled_numbers(int(a),int(b)))+"\n")
