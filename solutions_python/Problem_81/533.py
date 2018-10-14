def print_matrix(m):
	for line in m:
		print line
		
def solve(n,arr):
	#print_matrix(arr)
	wpArrW=[]
	wpArrT=[]
	wpArr=[]
	tPlayes=[]
	for i in range(len(arr)):
		#count=0
		win=0
		tPlaye=[]
		for j in range(len(arr[i])):
			if arr[i][j]=='1': 
				win=win+1
				#count=count+1
			#if arr[i][j]=='0':
				#count=count+1
			if arr[i][j]!='.':
				tPlaye.append(j)
		wpArrW.append(win)
		wpArrT.append(len(tPlaye)) #wpArrT.append(count)
		wpArr.append(float(win)/len(tPlaye))#wpArr.append(float(win)/count)
		tPlayes.append(tPlaye)
	print 'wp', wpArr
	print 'tPlayes', tPlayes
	print '------------------------'
	owpArrW=[]
	owpArrT=[]
	owpArr=[]
	
	for i in range(len(wpArrW)):
		sumWS=0
		for op in range(len(tPlayes[i])):
			wonMe=0
			#print 'if' , i,'wom->', tPlayes[i][op]
			if (arr[tPlayes[i][op]][i])=='1':
				wonMe=1
			wons=wpArrW[tPlayes[i][op]]-wonMe
			#print 'wons:',wpArrW[tPlayes[i][op]],wonMe
			game=0
			if (arr[tPlayes[i][op]][i])!='.':
				game=1
			total=wpArrT[tPlayes[i][op]]-game
			wsP=float(wons)/(total)
			sumWS=sumWS+wsP
			#print 'op:',op,'---',wons,total,wsP
		#print '----->', sumWS, len(tPlayes[i]), float(sumWS)/len(tPlayes[i])
		owpArr.append(float(sumWS)/len(tPlayes[i]))
	print 'owp', owpArr
	
	oowpArr=[]
	for i in range(len(wpArrW)):
		sum=0
		for op in range(len(tPlayes[i])):
			sum=sum+owpArr[tPlayes[i][op]]
		oowpArr.append(float(sum)/len(tPlayes[i]))
	
	RPI=[]
	for i in range(n):
		RPI.append(0.25 * wpArr[i] + 0.50 * owpArr[i] + 0.25 * oowpArr[i])
	return RPI
	
#main
from time import time
if __name__ == "__main__":
	def getInts():
		return map(int, input.readline().rstrip('\n').split(' '))
	start_time=time()
	output = open('C:/Users/Jenny/Desktop/gcj/output', 'w')
	input = open("C:/Users/Jenny/Desktop/gcj/in.txt", "r")
	T = int(input.readline())
	for case in range(1, T + 1):
		n=getInts()
		p=[]
		for line in range(n[0]):
			p.append(list(input.readline().rstrip('\n')))
		ans = solve(n[0],p)
		s = "Case #%d:\n" %(case)
		for i in range(len(ans)):
			s=s+str(ans[i])+"\n"
		print s,
		output.write(s)
	print "Total time: %d msec"%(1000*(time()-start_time))