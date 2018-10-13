import sys;
dict={'y':'a','n':'b','f':'c','i':'d','c':'e','w':'f','l':'g','b':'h','k':'i','u':'j','o':'k','m':'l','x':'m','s':'n','e':'o','v':'p','z':'q','p':'r','d':'s','r':'t','j':'u','g':'v','t':'w','h':'x','a':'y','q':'z'}
list1=list()
string=""
new_output=""
word=""
f=open("small.in","r")
f_out=open("out.txt","w")
lines=f.readlines()
no_input=int(lines[0][:-1])
print no_input
#string=raw_input("Enter string")
for l in range(1,no_input+1):
	list1=lines[l][:-1].split(" ")
	new_output="Case #"+str(l)+": "	
	for i in list1:
		for j in i:
			word=word+dict[j]
		new_output=new_output+word+" "
		word=""
	
	f_out.write(new_output+"\n")
	new_output=""
f_out.close()	
