# Google Code Jam 2012 Googlerese
# Javier Fernandez javierfdr@gmail.com, javierfdr


import sys

def parse_file(in_file):
	num_cases = int(in_file.readline())
	case_list = []
	for c in range(num_cases):
		case = in_file.readline().strip('\n')
		case_list.append(case)
	return case_list

	
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','u','w','x','y','z']	
invere_match = {
'a':'y',
'b':'n',
'c':'f', #guessed :(
'd':'i',
'e':'c',
'f':'w',
'g':'l',
'h':'b',
'i':'k',
'j':'u',
'k':'o',
'l':'m',
'm':'x',
'n':'s',
'o':'e',
'p':'v',
'q':'z', #guessed :(
'r':'p',
's':'d',
't':'r',
'u':'j',
'v':'g',
'w':'t',
'x':'h',
'y':'a',
'z':'q'
}

match = {
'y':'a',
'n':'b',
'f':'c', #guessed :(
'i':'d',
'c':'e',
'w':'f',
'l':'g',
'b':'h',
'k':'i',
'u':'j',
'o':'k',
'm':'l',
'x':'m',
's':'n',
'e':'o',
'v':'p',
'z':'q', #guessed :(
'p':'r',
'd':'s',
'r':'t',
'j':'u',
'g':'v',
't':'w',
'h':'x',
'a':'y',
'q':'z',
' ':' '
}

def find(letter,match):
	for key in match.keys():
		if(match[key]==letter):
			return True
	return False
	
def get_phrase_trans(word, match):
	trans=''
	for letter in word:
		trans+=match[letter]
	return trans

out_file = open('output.out','w+')
in_file = sys.stdin
case_list = parse_file(in_file)
count = 1
for word in case_list :
	trans = get_phrase_trans(word,match)
	#print "Case #"+str(count)+": "+str(trans)
	out_file.write("Case #"+str(count)+": "+str(trans)+"\n")
	count+=1
#for c in range(1,num_cases+1):
#	case = 'Case #'+str(c)+': '
#	result= case+ str(size_of_loop(blue_list[c-1],red_list[c-1]))+'\n'
#	out_file.write(result)

