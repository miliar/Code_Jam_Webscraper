def solve(matrix):
    for y in range(len(matrix) - 1):
        for x in range(len(matrix[0]) - 1):
            center = int(matrix[y][x])
            op = int(matrix[y+1][x+1])
            if op > center:
                if int(matrix[y][x+1]) > center and int(matrix[y+1][x]) > center:
                    return "NO"
            elif op < center:
                if int(matrix[y][x+1]) != op and int(matrix[y+1][x]) != op:
                    return "NO"
                            
            else:
                if int(matrix[y][x+1]) != op and int(matrix[y+1][x]) != op:
                    return "NO"

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            for t in range(len(matrix)):
                for u in range(len(matrix[y])):
                    if u != x and t != y:
                        center = int(matrix[y][x])
                        if int(matrix[t][u]) >= center and (int(matrix[t][x]) < center or int(matrix[y][u]) < center):
                            return "NO"

            
            
    return "YES"



f  = open("B-small-attempt2.in","r")
tests = int(f.readline())
test = 1
print(tests)
lines = f.readlines()
f.close()


w = open('outtest.txt',"w")
pos = 0
for test in range(tests):
    matrix = []
    dim = lines[pos].split()
    pos = pos + 1
    for x in range(int(dim[0])):
        matrix.append(lines[pos + x].split())
    ans = solve(matrix)
    w.write("Case #" + str(test + 1) + ": " + ans + "\n")
    print("Case #" + str(test + 1) + ": " + ans + "\n")
    pos = pos + int(dim[0])
            
w.close()
