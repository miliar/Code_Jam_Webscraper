import sys
import os

input_file_name = "C-small-1-attempt1 (1).in"

def router_old(stalls, bathroom):
	
	distances = []
	# Calculate distances
	for i in range(len(bathroom)):
		L = 0
		R = 0
		if bathroom[i] == False:
			for l in range(i-1,0,-1):
				if bathroom[l] == True:
					break
				else:
					L+=1
			for r in range(i+1,len(bathroom)):
				if bathroom[r] == True:
					break
				else:
					R+=1
			distances.append([L,R])
		else:
			distances.append(None)
	
	# Preferences: dictionary with keys = minimum distance, values = stall indexes
	preferences = {}
	for d in range(1,len(distances)-1):
		if distances[d] == None:
			continue
		key = min(distances[d])
		if key in preferences:
			preferences[key].append(d)
		else:
			preferences[key] = [d]

	a = max(preferences.keys())
	filtered = preferences[a]
	print(filtered)
	if len(preferences[a]) > 1:
		i = 1
		while i < len(filtered):
			first = max(distances[filtered[i-1]])
			second = max(distances[filtered[i]])
			if first != second:
				print("Deleted")
				print(distances[filtered[i]])
				first = max(distances[filtered[i-1]])
				second = max(distances[filtered[i]])
				
				if first > second:
					del filtered[i]
				else:
					del filtered[i-1]
			else:
				i+=1
	
	filtered.sort()
	chosen_bathroom = filtered[0]
	bathroom[chosen_bathroom] = True
	print(filtered)
	print(bathroom)
	print(distances)
	print(preferences)
	return (max(distances[chosen_bathroom]), min(distances[chosen_bathroom]))

def router(stalls, busy):
	busy.sort()
	best_place = {"dist": 0, "coord": None}
	
	for i in range(1,len(busy)):
		if busy[i]-busy[i-1] > best_place["dist"]:
			best_place["dist"] = busy[i]-busy[i-1]-1
			best_place["coord"] = [busy[i-1], busy[i]]
	print(best_place)
	if best_place["dist"] % 2 == 1:
		busy.append(best_place["coord"][0]+best_place["dist"]/2+1)
		print(busy)
		return [best_place["dist"]/2, best_place["dist"]/2]
	else:
		busy.append(best_place["coord"][0]+best_place["dist"]/2)
		print(busy)
		return [best_place["dist"]/2, best_place["dist"]/2-1]

with open(input_file_name, "r") as input_file:
	cases = int(input_file.readline())
	results = []
	#input_file.readline()
	# input_file.readline()
	for line in input_file:
		line = line.split(" ")
		stalls = int(line[0])+2
		people = int(line[1])
		bathroom = [True]+[False]*stalls+[True]
		print("Stalls: "+str(stalls))
		print("People: "+str(people))
		sys.stdout = open(os.devnull, "w")
		busy = [1, stalls]
		for visit in range(people):
			last_visit = router(stalls, busy)
		sys.stdout = sys.__stdout__
		print(last_visit)
		results.append(last_visit)
		#break

with open(input_file_name.split('.')[0]+"_results", "w") as output_file:
	print("")
	print("WRITING RESULTS TO FILE")
	for i in range(len(results)):
		output_string = "Case #"+str(i+1)+": "+str(results[i][0])+" "+str(results[i][1])
		print(output_string)
		output_file.write(output_string+"\n")
