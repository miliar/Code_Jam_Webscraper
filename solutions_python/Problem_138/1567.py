import bisect

f = open('D-large.in', 'r')
g = open('output.txt', 'w')
n = int(f.readline())
for i in range (1, n+1):
    weights = int(f.readline())
    found = 0
    string1 = f.readline()
    string2 = f.readline()
    weightsnaomi = string1.split()
    weightsken = string2.split()
    weightsnaomi = [float(x) for x in weightsnaomi]
    weightsken = [float(x) for x in weightsken]    
    naomi = sorted(weightsnaomi)
    ken = sorted(weightsken)
    warpoints = 0
    deceitfulwarpoints = 0
    for j in range (0, weights):
    	chosennaomi = naomi[j]
    	indexken = bisect.bisect(ken,chosennaomi)
    	if indexken == len(ken):
    	    warpoints = warpoints + len(ken)
    	    break
    	del ken[indexken]
    naomideceitful = sorted(weightsnaomi, reverse=True)
    ken = sorted(weightsken)
    deceitful = sorted(weightsken, reverse=True)
    for j in range (0, weights):    
        chosennaomi = naomi[0]
        highestken = deceitful[0]         
        toldnaomi = naomideceitful[0]
    	indexken = bisect.bisect(ken,toldnaomi)
    	chosenken = ken[0]
    	if indexken != len(ken):
    	    chosenken = ken[indexken]
    	if chosenken < toldnaomi:
    	    chosennaomi = naomi[bisect.bisect(naomi, chosenken)]
    	    deceitfulwarpoints = deceitfulwarpoints + 1
    	naomi.remove(chosennaomi)
    	ken.remove(chosenken)  
    	naomideceitful.remove(chosennaomi)
    	deceitful.remove(chosenken)
    
    line = 'Case #' + str(i) + ': ' + str(deceitfulwarpoints) + ' ' + str(warpoints) + '\n'
    g.write(line) 
f.close()
g.close()