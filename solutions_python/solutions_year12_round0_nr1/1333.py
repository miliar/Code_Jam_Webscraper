file=open('A-small-attempt0.in','r')
text=file.read()
text=text.split('\n')
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
alphabet2=['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q',' ']
a=1
answer2=[]
answer=[]
while a<=30:
	answer2=[]
	file=text[a].split('0')
	file="".join(file)
	length=len(file)
	b=0
	file=list(file)
	while b<length:
		number=str(file[b])
		index=alphabet2.index(number)
		letter=alphabet[index]
		letter=str(letter)
		answer2.append(letter)
		answers=answer2
		b=b+1
	answer2="".join(answer2)
	answer2="Case #"+`a`+": " + answer2
	answer.append(answer2)
	a=a+1
answer="\n".join(answer)
file2=open('output.txt','w')
file2.writelines(answer)
file2.close()