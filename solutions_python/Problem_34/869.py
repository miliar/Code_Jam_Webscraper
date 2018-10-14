L=0
D=0
N=0
word_list=[]
new_word=''
s=''
split_list=[]
split=0
count=0
x=1
file_output=open('output.txt','w')
file_input=open('input.txt','r')

s=file_input.readline()
s=s.rstrip('\n')
split_list=s.split(' ')
L=int(split_list[0])
D=int(split_list[1])
N=int(split_list[2])
split=D

def recurse_list(list_index,element_index,current_word):
	global count
	if list_index < L-1:
		for i in range(0,len(split_list[list_index+1])):
			string_new=''
			string_new=current_word + split_list[list_index+1][i]
			recurse_list(list_index + 1, i, string_new)
			print string_new
			if string_new in word_list:
				print string_new
				count = count+1
		
def find_existence():
	global count
	for i in range(0,D):
		exist=0
		for j in range(0,L):
			#print word_list[i][j], split_list[j]
			if word_list[i][j] in split_list[j]:
				exist=exist+1
				print 'true',exist,i,j
			else:
				j=L-1
		if exist==L:
			count=count+1
			print count			
		
while split>0:
	new_word=file_input.readline()
	new_word=new_word.rstrip('\n')
	length=len(new_word)
	if length!=L :
		print 'last word not accepted'
	else :
		word_list.append(new_word)
		split=split-1

while N>0:
	count=0
	s=file_input.readline()
	s=s.rstrip('\n')
	length=len(s)
	string_new=''
	split_list=[]
	add=0
	for i in range(0,length):
		if s[i]=='(':
			add=1
		elif s[i]==')':
			add=0
			split_list.append(string_new)
			string_new=''
		elif add==1:
			string_new=string_new+s[i]
		else:
			split_list.append(s[i])			
	
	#for i in range(0,len(split_list[0])):
	#	recurse_list(0,0,split_list[0][i])		
	find_existence()
	print "Case #"+str(x)+": "+str(count)
	file_output.write("Case #"+str(x)+": "+str(count)+"\n")
	N = N-1
	x=x+1

file_input.close()
file_output.close()
