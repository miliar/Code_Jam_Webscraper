def firstOn(N):
    aux = 1
    
    for i in range(1,N):
        aux = 2*aux +1

    return aux


def isOn(N,K):
    bn = list(bin(K)[2:])
    bn.reverse()
    bn = bn[:N]
    bn = list(bn)
    for i in range(N-len(bn)):
        bn.append(0)
    #print(bn)
    on = True
    for b in bn:
        if b != "1":
            return "OFF"

    return "ON"


def main():
    fileIn = open("in.in")
    fileOut = open("out.out","w")

    lines = fileIn.read().split("\n")
    nCase = int(lines[0])
    index = 1
    for index in range(1,nCase+1):

        line = lines[index].split()

        N = int(line[0])
        K = int(line[1])

        #fileOut.write(str(N)+"\t"+str(K)+"\n")
        fileOut.write("Case #"+str(index)+": "+isOn(N,K)+"\n")
        index+=1

    fileIn.close()
    fileOut.close()

main()

#print(isOn(30,(10**9)+2))
