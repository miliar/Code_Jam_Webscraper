from math import log
from operator import itemgetter
t=int(raw_input())
for tt in range(0,t):
	n,k=map(int,raw_input().split())
	d=dict()
	i=1
	print 'Case #'+str(tt+1)+':',
	mid = (0+n)/2
	num=1
	f=0
	l=n
	if n==k:
		print 0,0
	elif k==1:
		print max(mid-f,l-mid-1),min(mid-f,l-mid-1)
	#elif int(log(n)/log(2))==int(log(k)/log(2)):
		# xx = 0
		# pp=1
		# for xxx in range(0,int(log(k)/log(2))):
		# 	xx+=(pp)
		# 	pp=pp*2
		# qq = k-xx
		# if qq==1 and n%2==0:
		# 	print 1,0
		# else:
		#print 0,0
	else:
		level_k = int((log(k)/log(2))) + 1
		while num<int(log(n)/log(2))+1:
			start = 2**(num-1)
			end = start*2
			count=end
			index_counter=start/2
			ff=0
			for i in range(start,end):
				if f==0 and l==n:
					pass
				else:
					if ff==0:
						f=d[index_counter][0][1]
						l=d[index_counter][0][2]
						ff+=1
					else:
						f =d[index_counter][1][1]
						l=d[index_counter][1][2]
						ff=0
						index_counter+=1
				mid = (f+l)/2
				d[i] = [[count,f,mid],[count+1,mid+1,l]]
				f=0
				l=0
				count+=2
			if num+1==level_k:
				xx = 0
				pp=1
				for xxx in range(0,num):
					xx+=(pp)
					pp=pp*2
				qq = k-xx
				dis=[]
				for i in range(start,end):
					mid1=(d[i][0][1] +d[i][0][2])/2
					mid2= (d[i][1][1] +d[i][1][2])/2
					dis.append([min(mid1- d[i][0][1],max(d[i][0][2] -mid1-1,0)),max(mid1- d[i][0][1],max(d[i][0][2] -mid1-1,0))])
					dis.append([min(mid2- d[i][1][1],  max(d[i][1][2] -mid2-1,0)), max(mid2- d[i][1][1],  max(d[i][1][2] -mid2-1,0))])
					#dis.append([ mid1- d[i][0][1],  max(d[i][0][2] -mid1-1,0)])
					#dis.append([ mid2- d[i][1][1],  max(d[i][1][2] -mid2-1,0)])
				#print dis
				dis = sorted(dis,key=itemgetter(0,1))
				dis.reverse()
				#print dis
				#print dis
				# size=(end-start)
				# vis = [0]*(size*2)
				# cc=0
				# index=0
				# while cc< qq:
				# 	cc+=1
				# 	index = -1
				# 	mini=-1
				# 	maxi=-1
				# 	for i in range(0,size*2):
				# 		if vis[i]==0:
				# 			if min(dis[i])>mini:
				# 				index=i
				# 				mini = min(dis[i])
				# 				maxi = max(dis[i])
				# 			elif min(dis[i])==mini:
				# 				if maxi<max(dis[i]):
				# 					index=i
				# 					mini = min(dis[i])
				# 					maxi = max(dis[i])
				# 	vis[index]=1
				#print vis
				print dis[qq-1][1],dis[qq-1][0]#max(dis[index]),min(dis[index])
				# if qq>(end)/2:
				# 	qq-=(end/2)
				# 	ppp=1
				# 	for jjj in range(1,qq):
				# 		ppp+=2
				# 	print max(dis[ppp]),min(dis[ppp])
					# if min(dis[ppp])==-1:
					# 	print 0
					# else:
					# 	print min(dis[ppp])
				# else:
				# 	ppp=0
				# 	for jjj in range(1,qq):
				# 		ppp=ppp+2
				# 	print max(dis[ppp]),min(dis[ppp])
					# if min(dis[ppp])==-1:
					# 	print 0
					# else:
					# 	print min(dis[ppp])
				break
			num+=1