f = open("A-large.in", "r")
#f = open("input.txt", "r")
num_cases = int(f.readline())
cases = []
for c in range(num_cases):
    cases.append(f.readline())
    
def processCase(case):
    tok = case.split()
    #print tok
    max_shyness = int(tok[0])
    shy_array = [0]*(max_shyness+1)
    #print max_shyness, "mx"
    for x in range(max_shyness+1):
        shy_array[x] = int(tok[1][x])
    return [max_shyness, shy_array]

def processTest(test):
    standing = 0
    friends = 0
    for x in range(test[0]+1):
        #print x, 'x', standing, 's', friends, "in"
        if x == test[0]+1:
            break
        if standing >= x:
            standing += test[1][x]
        else:
            friends += x - standing
            standing += x-standing + test[1][x]
        #print x, 'x', standing, 's', friends, "out"
    return friends

cnum = 1
g = open("large-out.txt", "w")
for c in cases:
    #print processCase(c)
    value = processTest(processCase(c))
    #print("Case #{}: {}".format(cnum, value))
    g.write("Case #{}: {}\n".format(cnum, value))
    cnum+=1