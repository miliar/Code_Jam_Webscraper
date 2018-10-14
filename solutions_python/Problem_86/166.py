def solve(notes, l, h):

    for i in range(l, h+1):
        flag = 0
        for note in notes:
            bigger = smaller = 0
            bigger = max(i, note)
            smaller = min(i, note)
            #print i, note, i%note
            if bigger%smaller != 0: flag += 1
        if flag == 0:
            return i
    else:
        return "NO"
        
                
input = open('C-small-attempt0.in', 'r')
output = open('c.out', 'w')

t = int(input.readline())
for case in range(1, t+1):
   
    n, l, h = map(int, input.readline().strip().split())
    notes = map(int, input.readline().strip().split())

    #print n, l, h, notes
    
    result = solve(notes, l, h)

    print 'Case #'+str(case)+':', result
    #print
    output.write("Case #%s: %s\n" %(case, result))
