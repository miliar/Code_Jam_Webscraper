import time

s_time=time.time()


f= open('A-small-attempt0.in','r')
#f= open('testa.in','r')
q= open('aresult.out','w')

vowel=['a','e','i','o','u']

def tribe_location(name,n):
	visited=set()
	total=0
	length=len(name)
	for i in range(length-n+1):
		mark=True
		for j in range(n):
			if name[i+j] in vowel:
				mark=False
		if mark:
			visited.add(i)	
			####to left
			l=0
			r=0
			if i>=1:
				for left in range(i-1,-1,-1):
					if left in visited:
						break
					l+= 1
					
			######to right
			if i+n<length:
				for right in range(i+n,length):
					if right in visited:
						break				
					r +=1
					
			
			total +=(1+l+r+r*l)
	return total

f.readline()
count=1

for line in f:
    name,n=line[:-1].split(' ')
    n=int(n)
    #print tribe_location(name,n)    
    s='Case #'+str(count)+': '+str(tribe_location(name,n))+'\n'  
    count +=1  
    q.write(s)
    print 'ok'+str(count-1)
        
                
f.close()
q.close()
print 'seconds:',time.time()-s_time







