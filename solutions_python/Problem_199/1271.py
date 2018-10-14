

cases = int(input())

def solve(cakes,k):
    counter = 0
    for i in range(0,len(cakes)-k+1):
        if cakes[i] == 0:
            counter += 1
            for j in range(0,k):
                if cakes[i+j] == 0:
                    cakes[i+j] = 1
                else:
                    cakes[i+j] = 0
    for i in cakes:
        if i == 0: return("IMPOSSIBLE")
    return str(counter)


for i in range(0,cases):
    inflow = str(input()).split(' ')
    incakes = inflow[0]
    spatula = int(inflow[1])
    integer_cakes = []
    for j in incakes:
        if j == '+':
            integer_cakes.append(1)
        else:
            integer_cakes.append(0)
    print("Case #"+str(i+1)+": "+ solve(integer_cakes,spatula))
            




#solve([1,0,1,1,1,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0],4)
