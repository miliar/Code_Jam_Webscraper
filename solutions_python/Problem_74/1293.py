#first line is number of cases
#lines contain
# number of entries + entries
#a=raw_input()
import time
file = open("A-large.in")
N=int(file.readline())
r=0
orange_current_pos=1
blue_current_pos=1
tot_time=0
blue_space=0
orange_space=0
last_pressed=0

while r<N:

	line = file.readline()
	values=line.split()
	entries=int(values[0])
	for i in range(1,((entries*2)+1),2):
		if(values[i]=="O"):
			orange_moveto=int(values[i+1])
			o_state="move"
		
			while o_state!="pressed":
				if(orange_current_pos==orange_moveto):
					if(tot_time>=last_pressed):
						o_state="pressed"
						tot_time=tot_time+1
						last_pressed=tot_time
						blue_space=0
						orange_space+=1
					else:
						tot_time+=1

				else:
					o_state="move"
					if(orange_current_pos>orange_moveto):
						orange_current_pos-=1
					else:
						orange_current_pos+=1
					if(blue_space!=0):
						blue_space=blue_space-1
					else:
						tot_time=tot_time+1
						orange_space+=1

		else:
			blue_moveto=int(values[i+1])
			b_state="move"
			while b_state!="pressed":
				if(blue_current_pos==blue_moveto):
					if(tot_time>=last_pressed):
						b_state="pressed"
						tot_time=tot_time+1
						orange_space=0
						last_pressed=tot_time
						blue_space+=1	
					else:
						tot_time+=1
				else:
					b_state="move"
					if(blue_current_pos>blue_moveto):
						blue_current_pos-=1
					else:
						blue_current_pos+=1
			
					if(orange_space!=0):
						orange_space=orange_space-1
					else:
						tot_time=tot_time+1
						blue_space+=1
		
	print "Case #"+str(r+1)+": "+str(tot_time)
	tot_time=0
	orange_current_pos=1
	blue_current_pos=1
	tot_time=0
	blue_space=0
	orange_space=0
	last_pressed=0
	r+=1


