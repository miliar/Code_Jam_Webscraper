fin = open("D-large.in","r")
fout = open("output.txt","w")

t = int(fin.readline()[:-1])
i = 0

while i < t :
    n = int(fin.readline()[:-1])
    naomi = list(map(float,fin.readline()[:-1].split()))
    ken = list(map(float,fin.readline()[:-1].split()))
    
    #legal
    naomi.sort(reverse = True)
    ken.sort()
    ken_bool = []
    for j in range(n):
        ken_bool.append(False)
    counter1 = 0
    for k in range(len(naomi)):
        found = False
        for x in range(len(ken)):
            if ken[x] > naomi[k] and ken_bool[x] == False:
                ken_bool[x] = True
                found = True
                break
        if found == False:
            for y in range(len(ken)):
                if ken_bool[y] == False :
                    ken_bool[y] = True
                    counter1 += 1
                    break

    #illegal
    naomi.sort()
    counter2 = 0
    a = 0
    for b in range(len(naomi)):
        min_naomi = naomi[b]
        min_ken = ken[a]
        if min_naomi > min_ken :
            counter2 += 1
            a += 1
    i += 1
    #print(counter2,counter1)
    fout.write("Case #" + str(i) + ": " + str(counter2) + " " + str(counter1) + '\n')
fout.close()  
    
    
    
             
        
    
