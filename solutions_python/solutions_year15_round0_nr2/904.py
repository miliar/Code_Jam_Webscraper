f = open('B-small-attempt1.in', 'r')
#f = open('test.in', 'r')
g = open('output.txt', 'w')

def solve(Pi):
    t = 0
    max_p = max(Pi)
    if max_p <= 3:
        t = max_p
        return t
    else:
        no_interrupt = [i-1 for i in Pi]
        interrupt = [i for i in Pi]
        interrupt.remove(max_p)
        if max_p < 9:
            interrupt.append(max_p/2)
            interrupt.append(max_p - max_p / 2)
        else:
            interrupt.append(6)
            interrupt.append(3)
        t_n = solve(no_interrupt)
        t_i = solve(interrupt)
        return min(t_n, t_i)+1 
    
            
    
    


case = int(f.readline())
for index in range(1, case+1):
    D = int(f.readline())
    Pi = [int(i) for i in f.readline().split()]
    t = solve(Pi)
    print "Case #" + str(index) + ": " + str(t)
    g.write("Case #" + str(index) + ": " + str(t)+"\n")
