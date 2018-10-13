f = open("data.in","r")
x = []
for line in f:
	x.append(line.strip("\n"))
f.close()
x.pop()
p = [g.split(" ") for g in x]
counter = 0
for row in p[1:]:
	i=0
	c = int(row[i])
	i+=1
	combined_list = []
	for j in range(i,i+c):
		combined_list.append(row[j])
	d = int(row[i+c])
	i = i+c+1
	opposed_list = []
	for j in range(i,i+d):
		opposed_list.append(row[j])
	i = i+d+1
	strin=row[i]
	#print("combine:",combined_list)	
	#print("oppose:",opposed_list)
	#print(strin)
	final = []
	stringlist = list(strin)
	for char in stringlist:
	    if not final:
	        final.append(char)
	        continue
	    else:
	        last = final.pop()
	        alternative0 = char + last
	        alternative1 = last + char
	        found_combination = 0
	        for option in combined_list:
	            if option[0:2] == alternative1 or option[0:2] == alternative0 :
	                final.append(option[2])
	                char = option[2]
	                found_combination = 1
	                break
	        if found_combination == 0:
	            final.append(last)
	        found_opposition = 0
	        alpha = [x[1] for x in opposed_list if x[0] == char]
	        beta = [x[0] for x in opposed_list if x[1] == char]
	        opposing_chars = alpha + beta
	        for option in opposing_chars:
	            for s in final:
	                if option == s:
	                    found_opposition = 1
	                    final = []
	                    break
	            if found_opposition == 1:
	                break
	        if found_opposition == 0 and found_combination == 0:
	            final.append(char)
	print("Case #"+str(counter+1)+":",str(final).replace("'","")) 
	counter+=1 
print("")
