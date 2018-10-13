def decryptomus(text):
	keys={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
	new_string=''
	if len(text)<=2:
		return -1
	for s in text:
		if s!=' ':
			new_string=new_string+keys[s]
		else:
			new_string=new_string+' '
	return new_string
	
if __name__=="__main__":
	FILENAME='/Users/adityajitta/Downloads/A-small-attempt0.in.txt'
	fp=open(FILENAME,'r')
	num=0
	for line in fp:
		string_new=decryptomus(line.strip())
		if string_new != -1:
			num+=1
			print "Case #"+str(num)+": "+string_new