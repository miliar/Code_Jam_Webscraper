#
# google code jam problem alien langauge
#
import sys

def check_case(case_no,word,letter_tree,h):
    global num_cases
    h+=1
    if h>L:
	num_cases[case_no]+=1
	return
    i=0
    case_letters=[]
    while word[i]!='\n' and word[i]!='\r' :
	if word [i]==')':
		i+=1
		break
	if word[i]!='(':
		case_letters.append(word[i])
		if i==0:
		    i+=1		    
		    break
	i+=1
    remaining_word=word[i:]
    for	case_letter in case_letters:
	if letter_tree.has_key(case_letter):
			check_case(case_no,remaining_word,letter_tree[case_letter],h)
	else:
		continue	
  		
		
    
	


initial_input=sys.stdin.readline()
L,D,N=initial_input.split()
L=int(L)
D=int(D)
N=int(N)
words=[]
letter_tree={}
for  i in range(D):
    input=sys.stdin.readline()
    words.append(input)
    temp_tree=letter_tree
    for l in input:
	if not temp_tree.has_key(l):
       	    temp_tree[l]={}
	temp_tree=temp_tree[l]
test_cases=[]
num_cases=[]
for  i in range(N):
    input=sys.stdin.readline()
    test_cases.append(input)
    num_cases.append(0)
for i,case_word in enumerate(test_cases):
    check_case(i,case_word,letter_tree,0)
for i,case in enumerate(num_cases):
	print "Case #%s: %s" % (i+1,case)
