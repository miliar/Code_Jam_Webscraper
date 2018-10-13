def solve(S):
    a=int(S)/10
    e=0
    z=0
    x=0
    if(a<1):
        return S
    else:
        Y=str(S)
        while(e==0):        
            aux = len(Y)               
            while (x<=aux-1):
                #print (Y[x])
                while (z<=aux-1):
                    primero = Y[x]
                    segundo = Y[z]
                    if(Y[x]<=Y[z]):
                        e=1                        
                    else:
                        #print("Mirar Y[x]{0} Y[z]{1}".format(Y[x],Y[z]))
                        #print ("out")
                        e=0
                        x=aux
                        z=aux
                    z=z+1
                        #break   
                z=x+1
                x=x+1
            #print(e)
            if (e==0):   
                #print("Quito")
                Y=str(int(Y)-1)
                x=0
                z=0
        return Y

        
if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    """The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S, each character of which is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up). The string, when read left to right, represents the stack when viewed from top to bottom."""
    #f= open('A-small.in','r')
    T = int(f.readline())
    for case in range(1, T+1):
        S = f.readline().strip()
        solution = solve(S)
        print("Case #{0}: {1}".format(case, solution))