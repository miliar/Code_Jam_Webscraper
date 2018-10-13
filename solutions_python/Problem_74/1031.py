import sys


def find_sec(cases):
	n=int (cases[0])
	cnt=1;
	prev_o_pos=1
	prev_b_pos=1
	time=0
	b_time=0
	o_time=0
	while(cnt<=n*2):
		color=cases[cnt]
		pos=int(cases[cnt+1])
		if color=='O':
			temp_pos=abs(pos-prev_o_pos)
			if temp_pos>(time-o_time):
				time+=temp_pos-(time-o_time)
				time+=1
			else:
				time+=1
			o_time=time
			prev_o_pos=pos

		if color=='B':
			#print "pos",pos,"prev_b_pos",prev_b_pos
			temp_pos=abs(pos-prev_b_pos)
			if temp_pos>(time-b_time):
				#print "temp_pos=",temp_pos,"time",time,"b_time",b_time
				time+=temp_pos-(time-b_time)
				time+=1
				#print "t=",time,temp_pos,time-b_time
			else:
				time+=1
			b_time=time
			prev_b_pos=pos

		print "time=",time
		cnt=cnt+2
	return time
def main():
	print "hello"
	filename=sys.argv[1]
	fin=open(filename,"r")
	o=open("out.txt","w")
	k=0;
	for line in fin:
		if(k>0):
			cases=line.split()			
			print>>o,"Case #"+str(k)+":",str(find_sec(cases))
		k+=1;

if __name__=="__main__":
	main()
