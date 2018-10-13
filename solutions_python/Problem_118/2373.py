#!/usr/bin/python
def main():
	num=int(raw_input())
	for i in range(num):
		count=0
		limit=raw_input()
		limit=limit.strip()
		limit=limit.split()
		for j in range(int(limit[0]),int(limit[1])+1):
			if str(j)[::-1] == str(j):
				k= j** 0.5
				if int(str(k).split('.')[0]) == k:
					if str(int(k))[::-1]==str(int(k)):
						count+=1
		print 'Case #'+str(i+1)+': '+str(count)	

if __name__=="__main__":
	main()
