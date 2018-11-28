inpfile = open('C:/Users/Dane/Desktop/CJ/B-large.in','r')


def time1win(C,F,X,prod):
    a = C/prod
    return a + timewin(X,prod+F)

def timewin(X,producing):
    return X/float(producing)


def main():
    first = (int(inpfile.readline()))
    for i in range(0,first):
        print(first)
        cookies = 0
        producing = 2
        seconds = 0
        cont = True

        
        

        
        CFX = inpfile.readline()
        CFXDiv = CFX.split(' ')
        C = float(CFXDiv[0])
        F = float(CFXDiv[1])
        X = float(CFXDiv[2])

        while timewin(X,producing) > time1win(C,F,X,producing):
                seconds += timewin(C,producing)
                producing += F
                
                
        seconds += timewin(X,producing)
        with  open('C:/Users/Dane/Desktop/CJ/output2large.txt','a') as out1:
            out1.write('Case #%d: %.7f' % (i+1, seconds))
            out1.write('\n')
                
            
        
main()
