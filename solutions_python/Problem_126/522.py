import sys
#import math
from itertools import product
#import threading
#threading.stack_size(2*67108864) # 64MB stack
#sys.setrecursionlimit(2 ** 20)
def ProblemB(InputFileName):
	OutputFileName=InputFileName.replace('.in','.out')
	lines = open(InputFileName).read().splitlines()
	#f1=open(InputFileName)
	f2=open(OutputFileName,'w')
	vowels=set(['a', 'e', 'i', 'o', 'u'])
	T=int(lines[0])
	for t in range(1, T+1):
		name,n=lines[t].split()
		n=int(n)
		L=len(name)
		print name,n,
		#label cons (1) or not (0)
		nmlst=[]
		iscns=0
		for chr in name:
			if chr in vowels:iscns=0
			else:iscns=1
			nmlst.append(iscns)
		nmstr=''.join(map(str,nmlst))
		print nmstr,
		sbstr='1'*n
		#find all cons str of len n
		sbcnt=occurrences(nmstr,sbstr)
		print sbcnt,
		sta=[-1]*sbcnt
		nvset=set()
		for i in range(sbcnt):
			sta[i]=nmstr.find(sbstr,sta[i-1]+1)
			#print 'loop substrings'
			#print sta[i]
			for (s,e) in product(range(sta[i]+1),range(sta[i]+n-1,L)):
				#print s,e
				nvset.add((s,e))
		print sta, len(nvset)
		f2.write('Case #'+str(t)+': ' + str(len(nvset))+'\n')#, file=f)	
#stackoverflow.com/questions/2970520/string-count-with-overlapping-occurances
def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count
def main():	
	if len(sys.argv)==2: FileName=sys.argv[1]
	else: FileName='A-example.in'
	ProblemB(FileName)
# only new threads get the redefined stack size
# thread = threading.Thread(target=main)
# thread.start()
if __name__ == '__main__':
	main()