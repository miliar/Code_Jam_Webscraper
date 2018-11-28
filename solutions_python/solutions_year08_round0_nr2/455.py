import sys,os
import re
os.chdir(os.getcwdu() + "/Desktop")
f=open("input.txt","r")
f1=open("output.txt","w")
list=f.readline()
for i in range(0,int(list[:-1])):
	turnaround_time=int(f.readline()[:-1])
	number_of_trips=f.readline()[:-1]
	number_of_trips=re.split(" ",number_of_trips)
	NA=int(number_of_trips[0])
	NB=int(number_of_trips[1])
	NA_schedule=[]
	for j in range(0,NA):
		trip_time=f.readline()[:-1]
		trip_time=re.split(" ",trip_time)
		trip_time[0]=re.split(":",trip_time[0])
		trip_time[0]=int(trip_time[0][0])*60 + int(trip_time[0][1])
		trip_time[1]=re.split(":",trip_time[1])
		trip_time[1]=int(trip_time[1][0])*60 + int(trip_time[1][1])
		NA_schedule.append(trip_time)
	NA_schedule.sort()
	print NA_schedule
	NB_schedule=[]
	for j in range(0,NB):
		trip_time=f.readline()[:-1]
		trip_time=re.split(" ",trip_time)
		trip_time[0]=re.split(":",trip_time[0])
		trip_time[0]=int(trip_time[0][0])*60 + int(trip_time[0][1])
		trip_time[1]=re.split(":",trip_time[1])
		trip_time[1]=int(trip_time[1][0])*60 + int(trip_time[1][1])
		NB_schedule.append(trip_time)
	NB_schedule.sort()
	print NB_schedule
	temp=[]
	for k in NB_schedule:
		temp.append(k[1])
	count1=0
	loop=0
	temp.sort()
	if not temp==[]:
		for k in NA_schedule:
			print temp
			if not temp==[]:
				loop+=1
				if min(temp) <= k[0]- turnaround_time:
					temp.remove(temp[0])
					temp.sort()
				else:
					count1+=1
			else:
				count1+=NA-loop
	else:
		count1=NA
	print count1
	temp=[]
	for k in NA_schedule:
		temp.append(k[1])
	temp.sort()
	count2=0
	loop=0
	if not temp==[]:
		for k in NB_schedule:
			print temp
			if not temp==[]:
				loop+=1
				if min(temp) <= k[0]- turnaround_time:
					temp.remove(temp[0])
					temp.sort()
				else:
					count2+=1
			else:
				count2+=NB-loop
	else:
		count2=NB
	print count2
	f1.write("Case #" + str(i+1) + ": "+ str(count1) + " " + str(count2)) 
	f1.write("\n")
	
f.close()
f1.close()