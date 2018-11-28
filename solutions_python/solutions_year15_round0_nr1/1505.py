f = open('codeainput', 'r')
output = open('output', 'w')
T = int(f.readline())
#print "------------------"
for i in range(T):
    line = f.readline().split()
    S_max = int(line[0])
    S=[]
    for j in range(len(line[1])):
        S.append(int(line[1][j:j+1]))
        
    # print "S_Max = " +  str(S_max)
    # print "S = " + str(S)
    # print "------------------"
    count = S[0]
    needed = 0
    for j in range(1,len(S)):
        if count < j and needed < j:
            needed = j - count
        count += S[j]

    output.write( "Case #" + str(i+1) + ": " + str(needed) + "a\n")
output.close()    
f.close()
        
        
