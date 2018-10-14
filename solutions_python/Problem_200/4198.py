
def tatiana(x):

  length = len(str(x))
  word = str(x)
  y = list()
  z=0
  k=True
  while z<(length-1):
     if int(word[z])>int(word[z+1]):
       k=False
     z=z+1
  if k==True:
    return word
  else:
   z=0
   while z<(length-1):
      if int(word[z])<=int(word[z+1]):
        y.append(word[z])
      else:
        y.append(str(int(word[z])-1))
        break
      z=z+1
   y.append('9'*(length-1-z))
  
   strng=''.join(y)
   intgr=int(strng)
   sring=str(intgr)
   return tatiana(sring)
    
    



f=open('/home/sai/Downloads/B-large(1).in') # opens in read mode
g=open('/home/sai/Desktop/solB.out','w') # opens in write mode
f.readline()
counter=1
for i in f: #reads every line
	k=i.strip('\n') #inputs every line by stripping '\n'
	ans= tatiana(int(k))# computes the function
	g.write('Case #'+str(counter)+': '+str(ans)) #writes in file
	g.write('\n') # goes to new line
	counter+=1

f.close()	
g.close()
