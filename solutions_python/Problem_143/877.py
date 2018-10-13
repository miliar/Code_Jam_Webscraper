fin = open("B-small-attempt0.in", "r")
fout = open("output.txt","w")
t = int(fin.readline()[:-1])
i = 0


while i < t :
    
    a_b_k = list(map(int,fin.readline().split()))
    #print(a_b_k)
    way = 0
    for j in range(a_b_k[0]):
        for k in range(a_b_k[1]):
            if j & k < a_b_k[2] :
                way += 1
    
    i += 1
    
    fout.write("Case #" + str(i) + ": " + str(way)+ '\n')
                
fout.close()
