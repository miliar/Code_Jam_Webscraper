fi=open("A-small-attempt0.in",'r')#Input File 
#fi=open("A-large-practice.in",'r')#Input File 
#fi=open("A.in",'r')#Input File 
fo=open("A-small-attempt0.out","w")#Output File 
#fo=open("A-large-practice.out","w")#Output File 
 
mapping = {
	'a':'y',
	'b':'h',
	'c':'e',
	'd':'s',
	'e':'o',
	'f':'c',
	'g':'v',
	'h':'x',
	'i':'d',
	'j':'u',
	'k':'i',
	'l':'g',
	'm':'l',
	'n':'b',
	'o':'k',
	'p':'r',
	'q':'z',
	'r':'t',
	's':'n',
	't':'w',
	'u':'j',
	'v':'p',
	'w':'f',
	'x':'m',
	'y':'a',
	'z':'q',
	' ':' '
}

T=int(fi.readline()) 

for case in range(1,T+1,1): 
	g = fi.readline()
	ans = ''	
	for letter in (g):
		  if letter == '\n':
			break  	
		  ans += mapping[letter]	
	fo.write("Case #"+str(case)+": "+(ans)+"\n")
		
	
fi.close()
fo.close()	

