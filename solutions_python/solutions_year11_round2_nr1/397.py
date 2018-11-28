#!/usr/bin/python

def solve(records):
	wps = []
	for record in records:
		wins = record.count("1")
		losses = record.count("0")
		wps.append(float(wins)/(wins+losses))
	
	owps = []
	#totalOwp = 0.0
	for i in range(len(records)):
		avg = 0.0
		count = 0
		for record in records[0:i]+records[i+1:]:
			if record[i] != ".":	
				wins = record.count("1",0,i)+record.count("1",i+1)
				losses = record.count("0",0,i)+record.count("0",i+1)
				avg = avg + float(wins)/(wins+losses)
				count = count+1
			#if i == 3:
			#	print(str(float(wins)/(wins+losses)))
		avg = avg/count
		owps.append(avg)
	
	oowps = []
	for i in range(len(records)):
		total = 0.0
		count = 0
		for j in range(len(records[i])):
			if j != i and records[i][j] != ".":
				total = total + owps[j]
				count = count + 1
		oowps.append(total/count)
	
	result = []
	for i in range(len(records)):
		#print(str(wps[i])+" "+str(owps[i])+" "+str(oowps[i]))
		result.append((0.25*wps[i])+(0.5*owps[i])+(0.25*oowps[i]))
	return result

cases = int(raw_input())
for i in range(cases):
	teams = int(raw_input())
	records = []
	for j in range(teams):
		records.append(raw_input())
	output = "Case #"+str(i+1)+": "
	result = solve(records)
	for rpi in result:
		output = output+"\n"+str(rpi)
	print(output)
