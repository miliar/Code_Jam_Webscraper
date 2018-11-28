'''
Created on Apr 14, 2012
Google Code Jam 2012 Q2
@author: Dylan Hutchison
'''
if __name__ == '__main__':
    w = open("out.out", "w")
    f = open("test.in")
    T = int(f.readline())
    
    for tnum in range(1, T+1):
        line = f.readline().split()
        w.write("Case #"+str(tnum)+': ')
        N = int(line[0])
        S = int(line[1])
        p = int(line[2])
        
        numBest = 0
        if p == 0: # all Googlers have best score >= 0 
            numBest = N
        elif p == 1: # all Googlers with total score > 0 
            # have best score >= 1
            for token in line[3:]:
                if int(token) > 0:
                    numBest += 1
        else:
            trig = 3*p-2; # Googlers with total score >= trig
            # can have a best score >= p without surprise
            # trig - 2 <= total score < trig can have a best score if there is a surprise
            for token in line[3:]:
                if int(token) >= trig:
                    numBest += 1
                elif int(token) >= trig - 2:
                    if S > 0:
                        S -= 1
                        numBest += 1
        #we have numBest
        w.write(str(numBest)+'\n')
    f.close()
    w.close()
    
    