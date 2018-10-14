import sys


list_1={'1':'1', 'i':'i', 'j':'j', 'k':'k'}
list_i={'1':'i', 'i':'-1', 'j':'k', 'k':'-j'}
list_j={'1':'j', 'i':'-k', 'j':'-1', 'k':'i'}
list_k={'1':'k', 'i':'j', 'j':'-i', 'k':'-1'}

def test_str(data, X):
	complete_data=''
	for i in range(X):
		complete_data+=data

	current_data='1'
	sign=''
	goal=['i','j','k','1']
	count=0
	result=''
	curr_goal=goal[count]
	for i in range(len(complete_data)):
		if current_data=='1':
			result=list_1[complete_data[i]]
		elif current_data=='i':
			result=list_i[complete_data[i]]

		elif current_data=='j':
			result=list_j[complete_data[i]]

		elif current_data=='k':
			result=list_k[complete_data[i]]

		if result[0]=='-' and sign=='-':
			result=result[1:]
			sign=''
		if result[0]=='-' and sign=='':
			result=result[1:]
			sign='-'

		if result==curr_goal and sign=='':
			current_data='1'
			if count<3:
				count+=1
			curr_goal=goal[count]
		else:
			current_data=result
	#print "count = ", count
	if count==3 and current_data=='1' and sign=='':
		return 1
	else:
		return 0


f=sys.stdin
# fout=sys.stdout
case_num=int(f.readline())
#print case_num
for i in range(case_num):
	info=f.readline()
	#print info
	use=info.split()
	L=int(use[0])
	X=int(use[1])
	data=f.readline()
	data=data[:-1]
	
	if 	L*X<3 or (L*X==3 and data!='ijk') or L==1:
		print "Case #"+str(i+1)+": "+"NO"
	elif L*X==3 and data=='ijk':
		print "Case #"+str(i+1)+": "+"YES"
	else:
		if(test_str(data, X)==1):
			print "Case #"+str(i+1)+": "+"YES"
		else:
			print "Case #"+str(i+1)+": "+"NO"












# sys.stdout=fout
# fout.close()