import sys

def sol():
 fin = open('A-small-attempt1.in','r')
 fout = open('A-small.out','w')
 n = int(fin.readline());
 dic = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
 for j in range(0,n):
  str = fin.readline().replace('\n',"")
  pre = "Case #%d: "%(j+1)
  fout.write(pre)	
  for i in range(len(str)):
	if(str[i] == " "):
	 fout.write(str[i])
	else:
	 fout.write(dic[str[i]])
  fout.write('\n')
 fout.flush()
  