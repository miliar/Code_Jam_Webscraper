import time
import heapq
s_time=time.time()

def heapsort(data):
	result=[]
	heapq.heapify(data)
	while data:
		result.append(heapq.heappop(data))
	return result

def make_possible(A):
	op=0
	size=A
	tmp_op=999999
	while V:
		present = V.pop(0)
		if size>present:
			size +=present
		else:
			if size==1:
				return len(V)+1
			else:
				tmp_op = min(op+len(V)+1,tmp_op)
				while size <= present:
					size += size-1
					op +=1
				size += present
				if op >tmp_op:
					return tmp_op
	return min(op,tmp_op)




#f= open('A-large-practice.in','r')
f= open('A-large.in','r')
q= open('result.txt','w')

f.readline()
count=1
block=0
new_test=True

for line in f:
    if new_test:
        A,n = [int(n) for n in line[:-1].split(' ')]
        block=0
        new_test=False
        continue
    
    block +=1
    if block==1:  
    	V=heapsort([int(x) for x in line[:-1].split(' ')])
    	#print make_possible(V,A)
        s='Case #'+str(count)+': '+str(make_possible(A))+'\n'
        #print A,n,V
        count +=1  
        q.write(s)
        print 'ok'+str(count-1)
        new_test=True
                 
f.close()
q.close()
print 'seconds:',time.time()-s_time







