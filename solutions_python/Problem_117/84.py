import time

def solve(lawn): # check each 1 to see if it's not blocked
    for i in range(len(lawn)):
        for j in range(len(lawn[0])):
            if lawn[i][j] == 1:
                if (lawn[i].count(2) <> 0) \
                   and ([row[j] for row in lawn].count(2) <> 0):
                    return "NO"
    return "YES"

def solve_lrg(lawn): # check each number to see if it's not blocked by bigger ones
    for i in range(len(lawn)):
        for j in range(len(lawn[0])):
            num = lawn[i][j]
            if ([k>num for k in lawn[i]].count(True) > 0) \
               and ([l>num for l in [row[j] for row in lawn]].count(True) > 0):
                return "NO"
    return "YES"

    

def main():     
    start_time = time.time()
##    f = open("in.txt")
    f = open("B-large.in")
    ff = open("out.txt", "w")
    N = int(f.readline())
    ins = []
    dims = []
    for i in range(N):
        dim = f.readline().replace("\n", "").split()
        dims.append(dim)
        ins1 = []
        for i in range(int(dim[0])):
            ins1.append(f.readline().replace("\n", "").split())
        ins.append(ins1)
    ins = [[[int(column) for column in row] for row in table] for table in ins]

    c=1
    for i in ins:
        sol = solve_lrg(i)
        print "Case #" + str(c) + ": " + sol
        ff.write("Case #" + str(c) + ": " + sol + "\n")
        c+=1

    print "time: " + str(round(time.time()-start_time,2)) + "s"
    f.close()
    ff.close()

main()
