


def genCombinations(name, n):
    combinations = []
    for i in range(0,len(name)):
        for j in range(n,len(name)+1):
            if i+j <= len(name):
                combinations.append(name[i:(i+j)])
    return combinations
        
def countValid(combinations,n):
    vocals = ['a','e','i','o','u']
    valid = 0
    for c in combinations:
        cons = 0
        
        for i in range(0,len(c)):
            if(c[i] in vocals):
                cons = 0
            else:
                cons += 1
                if(cons) == n:
                    valid += 1
                    break
    return valid

    
    
if __name__ == "__main__":
    
    f = open('input.txt','r')    
    numCases = int(f.readline())
    i = 1
    f2 = open('output.txt','w')
    while(i <= numCases):
        line = f.readline()
        l = line.split(' ')
        name = l[0]
        n = int(l[1])
        combinations =  genCombinations(name, n)
        valid = countValid(combinations, n)
        print('Case #'+str(i)+': '+str(valid))
        i+= 1
        

        
