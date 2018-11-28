# Usage: python script.py <input_file> [<output_file>]
# If "output_file" isn't specified, the program simply write it to console.

import sys

input_file = open(sys.argv[1])
output_text = ""

def readline():
    return input_file.readline().split("\n")[0]

def trees( data ):
    n = int(data[0])
    A = int(data[1])
    B = int(data[2])
    C = int(data[3])
    D = int(data[4])
    x0 = int(data[5])
    y0 = int(data[6])
    M = int(data[7])
    X = x0
    Y = y0
    ret = []
    ret.append([X, Y])
    for j in range(n-1):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        ret.append([X, Y])
    return ret

def in_list( triang ):
    global triangles
    if( triang[0] < triang[1] ):
        aux = triang[0]
        triang[0] = triang[1]
        triang[1] = aux
    if( triang[1] < triang[2] ):
        aux = triang[1]
        triang[1] = triang[2]
        triang[2] = aux
    if( triang[0] < triang[1] ):
        aux = triang[0]
        triang[0] = triang[1]
        triang[1] = aux
    if( not triang in triangles ):
        triangles.append(triang)
        

def center_valid(center):
    return center[0] == int(center[0]) and center[1] == int(center[1])

num_tests = int( readline() )

for i in range(num_tests):
    data = trees(readline().split(" "))
    triangles = []
    for x in data:
        for y in data:
            if(x==y):
                break
            for z in data:
                if(x==z or y==z):
                    break
                if( center_valid([(x[0]+y[0]+z[0])/3.0, (x[1]+y[1]+z[1])/3.0]) ):
                    in_list([data.index(x),data.index(y),data.index(z)])
    print "Case #" + str(i+1) + ": " + str(len(triangles))
    output_text += "Case #" + str(i+1) + ": " + str(len(triangles)) + "\n"

input_file.close()

if(len(sys.argv) > 2):
    output_file = open(sys.argv[2], "w")
    output_file.write(output_text)
    output_file.close()
else:
    print output_text
