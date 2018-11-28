# Google Code Jam 2014, Problem B - Cookie Clicker Alpha
# Steven Stevanus - stevenstevanus@gmail.com

def calcSeq(C,F,X,seqs):
    total = 0
    f = 2
    for i in seqs:
        if i=='A':
            total += (C/f)
            f += F
        else:
            total += (X/f)
    return total
            
def CookieClickerAlpha():
    try:
        f_input = open("B-small-attempt0.in","r")
        f_output = open('B-small-attempt0.ou','w')
        case = int(f_input.readline().strip('\n'))
        for i in range(1,case+1):
            C,F,X = [float(j) for j in f_input.readline().strip('\n').split(' ')]
            result = calcSeq(C,F,X,'B')
            for j in range(1,1000000):
                seq = ('A'*j)+'B'
                tmp = calcSeq(C,F,X,seq)
                if tmp < result:
                    result = tmp
                else:
                    f_output.write('Case #'+str(i)+': '+str(round(result,7))+'\n')
                    break
    except:
        print ("Error Reading File!")

    f_input.close()
    f_output.close()

if __name__ == '__main__':
    CookieClickerAlpha()
    
                   
