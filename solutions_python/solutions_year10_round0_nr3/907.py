
def themeParkCase(R, maxPass, group):
    money = 0

    def turnStile(group):
        cPass = 0
        newGroup = group[:]
        for g in range(len(group)):
            car = cPass+group[g]
            if car <= maxPass:
               cPass=car
               newGroup.append(newGroup.pop(0))
            else:
                break
        return newGroup,cPass
        
    for i in range(R):
        turn = turnStile(group)
        money+=turn[1]
        group = turn[0]

    return money

def themeParkRunCases(T,DataSet):
    for i in range(T):
        print "Case #"+str(i+1)+": "+str(themeParkCase(*DataSet[i]))

def inputParser(f):
    def spaceParser(string, length):
        product = []
        for i in range(length):
            nextSpace = string.index(" ")
            product.append(int(string[:nextSpace]))
            string=string[nextSpace+1:]
        product.append(int(string))
        return product

    T = int(f.readline()[:-1])
    DataSet=[]

    for i in range(T-1):
        R,k,n = spaceParser(f.readline()[:-1],2)
        group = spaceParser(f.readline()[:-1],n-1)
        DataSet.append([R,k,group])

    R,k,n = spaceParser(f.readline()[:-1],2)
    group = spaceParser(f.readline()[:],n-1)
    DataSet.append([R,k,group])
    return DataSet, T


f =open("C-small-attempt1.in","r")
parsed = inputParser(f)
themeParkRunCases(parsed[1],parsed[0])

