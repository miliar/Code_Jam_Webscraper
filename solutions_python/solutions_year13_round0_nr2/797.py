def horizontal_check(e, x, y, w, h):
    for i in range(w):
        if e[x][y] < e[i][y]:
            return False
    return True

def vertical_check(e, x, y, w, h):
    for i in range(h):
        if e[x][y] < e[x][i]:
            return False
    return True
        
f = open('B-large.in', 'r')

set_count = int(f.readline())
results = []
for i in range(set_count):
    words = f.readline().split()
#     print(words)
    n = int(words[0])
    m = int(words[1])
    elements = [[0 for x in range(n)] for x in range(m)]
    for j in range(n):
        words = f.readline().split()
        for k in range(m):
            elements[k][j] = int(words[k])
            
    result = True
    for j in range(n):
        for k in range(m):
            if (horizontal_check(elements, k, j, m, n) or vertical_check(elements, k, j, m, n)) is False:
                result = False
                break
        if result is False:
            break
    if result:
        results.append("Case #" + str(i+1) + ": YES")
    else:
        results.append("Case #" + str(i+1) + ": NO")
    
#     line = f.readline()
#     print(elements[1][0])
    
    
f = open('B-large.out', 'w')            

for line in results:
    f.write(line + '\n')
print(set_count)