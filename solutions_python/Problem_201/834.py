##input = open('C-sample-input.txt', 'r')
##output = open('C-sample-output.txt', 'w')

##input = open('C-small-2-attempt0.in', 'r')
##output = open('C-small.out', 'w')

input = open('C-large.in', 'r')
output = open('C-large.out', 'w')

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def solve(n, k):
    if n == k:
        return "0 0"
    gaps = {n: 1}
    powerof2 = 1
    numleft = k
##    print gaps
    while numleft > powerof2:
##        print "numleft", numleft
##        print "power", powerof2
        newgaps = {}
        for x in sorted(gaps.keys(), reverse=True):
##            print 'x=', x
            right = x / 2
            left = (x-1) / 2
            if right in newgaps.keys():
                newgaps[right] += gaps[x]
            else:                    
                if powerof2 == 1:
                    newgaps[right] = 1
                else:
                    newgaps[right] = gaps[x]
            if left in newgaps.keys():
                newgaps[left] += gaps[x]
            else:
                if powerof2 == 1:
##                    print 'left =', left
##                    print 'powerof2/2=', str(gaps[x])
                    newgaps[left] = 1
                else:
##                    print 'left =', left
##                    print 'powerof2/2=', str(gaps[x])
                    newgaps[left] = gaps[x]
        gaps = {}
        for x in newgaps.keys():
            gaps[x] = newgaps[x]
##        print gaps
        numleft -= powerof2
        powerof2 *= 2
    if numleft == powerof2:
##        print 'in here'
        right = min(gaps) / 2
        left = (min(gaps) - 1) / 2
        return str(right) + " " + str(left)
##    print 'made it here'
    for x in sorted(gaps.keys(), reverse=True):
##        print 'x=', x
##        print 'numleft=', numleft
        if gaps[x] >= numleft:
            right = x / 2
            left = (x-1) / 2
            return str(right) + " " + str(left)
        else:
            numleft -= gaps[x]
    
            
    

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        n, k = read_ints()
##        if case == 7:        
        solution = solve(n, k)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        
##print solve(50, 9)
main()
input.close()
output.close()
    
