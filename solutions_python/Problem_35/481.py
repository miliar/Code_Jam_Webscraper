import psyco
psyco.full()

from string import lowercase

def main():
	tc=input()
	counter=1
	alphabetlist=list(lowercase)
	while(tc):
		tc-=1
		
		r,c=map(lambda x:int(x), raw_input().split())
		
		inputtc=[[0 for i in range(c)] for i in range(r)]
		
		outputtc=[[0 for i in range(c)] for i in range(r)]
		
		for i in range(r):
			inputtc[i]=map(lambda x:int(x), raw_input().split())

		for k in range(r*c):
			alphabetcount=0
			for i in range(r):
				for j in range(c):
				
					if i-1>=0:
						tn=inputtc[i-1][j]
					else:
						tn=10
					
					if j-1>=0:
						tw=inputtc[i][j-1]
					else:
						tw=10
				
					if j+1<c:
						te=inputtc[i][j+1]
					else:
						te=10
					
					if i+1<r:
						ts=inputtc[i+1][j]
					else:
						ts=10
					
					temp=[tn,tw,te,ts]
				
					temp=map(lambda x: x-inputtc[i][j], temp)
					indextemp=temp.index(min(temp))
				
					if min(temp)<0:
						if indextemp==3:
							if outputtc[i][j]==0 and outputtc[i+1][j]==0:
								outputtc[i][j]=alphabetlist[alphabetcount]
								outputtc[i+1][j]=alphabetlist[alphabetcount]
								alphabetcount+=1
							elif outputtc[i+1][j]==0:
								outputtc[i+1][j]=outputtc[i][j]
							else:
								outputtc[i][j]=outputtc[i+1][j]
							continue
					
						elif indextemp==2:
							if outputtc[i][j]==0 and outputtc[i][j+1]==0:
								outputtc[i][j]=alphabetlist[alphabetcount]
								outputtc[i][j+1]=alphabetlist[alphabetcount]
								alphabetcount+=1
							elif outputtc[i][j+1]==0:
								outputtc[i][j+1]=outputtc[i][j]
							else:
								outputtc[i][j]=outputtc[i][j+1]
							continue
					
						elif indextemp==1:
							if outputtc[i][j]==0 and outputtc[i][j-1]==0:
								outputtc[i][j]=alphabetlist[alphabetcount]
								outputtc[i][j-1]=alphabetlist[alphabetcount]
								alphabetcount+=1
							elif outputtc[i][j-1]==0:
								outputtc[i][j-1]=outputtc[i][j]
							else:
								outputtc[i][j]=outputtc[i][j-1]
							continue
					
						elif indextemp==0:
							if outputtc[i][j]==0 and outputtc[i-1][j]==0:
								outputtc[i][j]=alphabetlist[alphabetcount]
								outputtc[i-1][j]=alphabetlist[alphabetcount]
								alphabetcount+=1
							elif outputtc[i-1][j]==0:
								outputtc[i-1][j]=outputtc[i][j]
							else:
								outputtc[i][j]=outputtc[i-1][j]
							continue
				
					elif min(temp)>=0 and outputtc[i][j]==0:
						outputtc[i][j]=alphabetlist[alphabetcount]
						alphabetcount+=1
						continue
					elif min(temp)>=0 and outputtc[i][j]!=0:
						continue
					#To be iterated r*c times
		

		count=0
		dictionary={outputtc[0][0]:"a"}
		

		for i in range(r):
		  for j in range(c):
			if outputtc[i][j] in dictionary.keys():
			  outputtc[i][j]=dictionary[outputtc[i][j]]
			else:
				count+=1
				dictionary[outputtc[i][j]]=alphabetlist[count]
				outputtc[i][j]=dictionary[outputtc[i][j]]
				
		print "Case #%d:"%(counter)
		for k in xrange(r):
			for l in xrange(c):
				print outputtc[k][l],
			print
		counter+=1
			
main()
