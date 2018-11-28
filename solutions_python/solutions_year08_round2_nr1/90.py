fileinput = "A-small-attempt0.in"
fileoutput = "output.out"

#Library
def line2list(line,dest_type):
    temp = line.split(" ")
    return map(lambda x:dest_type(x),temp)

def array_contains(array,element):
    return element in array


f = file(fileinput)
data = f.read()
f.close()

output = ""

lines = data.split("\n")

cases = int(lines[0])

cindex = 0
cindex += 1
for case in range(1,cases + 1):

    count = 0

    vector = line2list(lines[cindex],int)
    [n, A, B, C, D, x0, y0 ,M] = vector

    trees = []

    X = x0
    Y = y0
    trees.append((X,Y))
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        trees.append((X,Y))

    for i in range(0,len(trees)):
        for j in range(i + 1,len(trees)):
            for k in range(j + 1,len(trees)):
                center = ((trees[i][0] + trees[j][0] + trees[k][0]) / 3.0, (trees[i][1] + trees[j][1] + trees[k][1]) / 3.0)
                #print center
                if (int(center[0]) == center[0]) and (int(center[1]) == center[1]):count += 1
                

    #print count

    #print trees
    output = output + "Case #"+str(case) + ": " + str(count) + "\n"
    cindex += 1


f2 = file(fileoutput,"w")
f2.write(output)
f2.close()

    

    

    
    
    
    
