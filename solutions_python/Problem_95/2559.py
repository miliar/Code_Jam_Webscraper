mp={'\n':'','f':'c','g':'v','d':'s',' ':' ','e':'o','b':'h','c':'e','a':'y','n':'b','o':'k','l':'g','m':'l','j':'u','k':'i','h':'x','i':'d','w':'f','v':'p','u':'j','t':'w','s':'n','r':'t','q':'z','p':'r','z':'q','y':'a','x':'m'};
fil=open('A-small-attempt0.in','r');
out=open('out.txt','w+');

n=int(fil.readline()); #number of sentences
re='';
for i in range(0,n):
	st=fil.readline();
	s='Case #'+str(i+1)+': ';
	for j in range(0,len(st)):
		s+=mp[st[j]];
	re+=s+'\n'
out.write(re);

out.close();
fil.close();