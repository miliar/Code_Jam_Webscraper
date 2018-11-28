

def check(l1,l2):
    count = 0
    ans = 0
    for i in range(4):
        for j in range(4):
            e1 = l1[i]
            e2 = l2[j]
            if e1 == e2:
                count += 1
                ans = e1
    if (count == 0):
        return -1 # did not find
    if (count == 1):
        return int(ans)
    if (count > 1):
        return -2 # more than 1
    
    
def get_sup(n):
    if (n == 0):
        return 0
    x = ceiling(n-1)
    return x+1
    
def get_nosup(n):
    x = ceiling(n)
    return x




def main():
    inpfile = open("A-small-attempt0.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    mp = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    mp2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        linelst = line.split()
        g1 = int(linelst[0])-1
  
        for i in range(4):
            line1 = inpfile.readline().strip()
            linelst1 = line1.split()   
            mp[i] = linelst1
            
        line = inpfile.readline().strip()
        linelst = line.split()
        g2 = int(linelst[0])-1
        
        for i in range(4):
            line1 = inpfile.readline().strip()
            linelst1 = line1.split()            
            mp2[i] = linelst1   
            
        #print "mp: " 
        #print mp
        #print "mp2: " 
        #print mp2
        
        
        n = check(mp[g1], mp2[g2])
        if n == -2:
            result = "Bad magician!"
        elif n == -1:
            result = "Volunteer cheated!"
        else:
            result = str(n)
        
        result = "Case #" + str(case) + ": " + result+"\n"
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":
    
    main()
    

    
    