infile = open("A-large.in","r")
outfile = open("A-large.txt","w")

def happy(b):
    if b == "+":
        return True
    return False

def range_sum_left(L,r,i):
    if i<r:
        return L[i]
    return L[i] - L[i-r]

def solve_left(s, k):
    l = len(s)
    sol_string = ""
    cummu_table = []
    count = 0
    if happy(s[0]):
        sol_string += "0"
        cummu_table.append(0)
    else:
        sol_string += "1"
        cummu_table.append(1)
        count += 1
    for i in range(1,l-k+1):
        b = s[i]
        flip = False
        cummu = range_sum_left(cummu_table, k-1, i-1)
        
        if happy(b):
            if cummu%2:
                flip = True
            else:
                flip = False
        else:
            if cummu%2:
                flip = False
            else:
                flip = True
        if flip:
            sol_string += "1"
            cummu_table.append(cummu_table[i-1]+1)
            count += 1
        else:
            sol_string += "0"
            cummu_table.append(cummu_table[i-1])
    return count, cummu_table
            
##def solve_right(s, k):
##    l = len(s)
##    sol_string = ""
##    cummu_table = []
##    count = 0
##    if happy(s[-1]):
##        sol_string += "0"
##        cummu_table.append(0)
##    else:
##        sol_string += "1"
##        cummu_table.append(1)
##        count += 1
##    for i in range(1,l-k+1):
##        b = s[-i-1]
##        flip = False
##        cummu = range_sum_left(cummu_table, k-1, i-1)
##        
##        if happy(b):
##            if cummu%2:
##                flip = True
##            else:
##                flip = False
##        else:
##            if cummu%2:
##                flip = False
##            else:
##                flip = True
##        if flip:
##            sol_string = "1" + sol_string
##            cummu_table.append(cummu_table[i-1]+1)
##            count += 1
##        else:
##            sol_string = "0" + sol_string
##            cummu_table.append(cummu_table[i-1])
##    return count, sol_string
def check(cummu_table, s, k):
    l = len(cummu_table)
    for i in range(1,k+1):
        b = s[-i]
        if i>l-1:
            flips = cummu_table[-1]
        else:
            flips = cummu_table[-1] - cummu_table[-1-i]
        flipped = flips%2
        if happy(b):
            if flipped:
                return False
        else:
            if not flipped:
                return False
    return True
def solve(s, k):
    c, t = solve_left(s,k)
    if check(t, s, k):
        return c
    return "IMPOSSIBLE"



t = int(infile.readline())
for case in range(1,1+t):
    s, k = infile.readline().split()
    s = s.strip()
    k = int(k)
    result = solve(s, k)
    outfile.write("Case #{}: {}\n".format(case, result))
outfile.close()
infile.close()
print("done")

            

        
            
            
