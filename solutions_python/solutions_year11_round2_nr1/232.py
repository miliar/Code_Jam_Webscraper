def calcWP(V1, WP):
    for i in xrange(len(V1)):
        won = 0.0
        lost = 0.0
        wpTemp = 0.0
        for j in xrange(len(V1[i])):
            if V1[i][j] == '1':
                won += 1.0
            if V1[i][j] == '0':                
                lost += 1.0
        wpTemp = won/(won+lost)
        WP.append(wpTemp)
    return 0

def getWP(V1, i, j):
    won = 0.0
    lost = 0.0
    owp = 0.0
    for k in xrange(len(V1[j])):
        if k != i:
          if V1[j][k] == '1':
              won += 1
          elif V1[j][k] == '0':
              lost += 1
    owp = won/(won+lost)
    return owp
    
def calcOWP(V1, OWP):
    for i in xrange(len(V1)):
        total = 0.0
        lost = 0.0
        owpTemp1 = 0.0
        owpTemp = []
        for j in xrange(len(V1[i])):
            if V1[i][j] == '1' or V1[i][j] == '0':
                owpTemp.append(getWP(V1, i, j))
                total += 1.0
        for k in xrange(len(owpTemp)):
            owpTemp1 += owpTemp[k]
        owpTemp1 = owpTemp1/(total)
        OWP.append(owpTemp1)
                  
    return 0
          
def calcOOWP(V1, OWP, OOWP):
    for i in xrange(len(V1)):
        total = 0.0
        oowpTemp = 0.0
        for j in xrange(len(V1[i])):
            if V1[i][j] == '1' or V1[i][j] == '0':
                oowpTemp += OWP[j]
                total += 1.0
        oowpTemp = oowpTemp/(total)
        OOWP.append(oowpTemp)
                  
    return 0
    
def prepare_input(input_file):
    test_case_count = int(input_file.readline())  #number of test cases
    
    output_file = file("A-large.out", "w")
    
    for test_case_counter in xrange(test_case_count):
        V1 = []
        lines1 = (input_file.readline().replace('\n','')).split(' ')
        N = int(lines1[0])
        for i in xrange(N):
          V1.append(input_file.readline().replace('\n',''))
        #print V1
        WP = []
        OWP = []
        OOWP = []
        calcWP(V1, WP)
        calcOWP(V1, OWP)
        calcOOWP(V1, OWP, OOWP)
        #print WP
        #print OWP
        #print OOWP
        output_file.write("Case #"+str(test_case_counter+1)+":\n") 
        for i in xrange(N):
            RPI = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]
            output_file.write(str(RPI) + "\n")
        #lowest count will be the number of switches in the server
        

    output_file.close()
    
if __name__ == "__main__":
    input_file = file("A-large.in")
    prepare_input(input_file)
