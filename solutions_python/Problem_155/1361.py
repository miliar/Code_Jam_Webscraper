f = open('A-large.in', 'r')
#f = open('input.in', 'r')
g = open('output.txt', 'w')

def solve(index, smax, si):
    if smax == 0:
        print "Case #" + str(index) + ": " + "0"
        g.write("Case #" + str(index) + ": " + "0"+"\n")
        return
    else:
        residual = 0
        non_shy = si[0]     # size of smax >= 1
        for i in range(smax):
            if non_shy >= i+1:
                non_shy += si[i+1]
            else:
                if si[i+1] > 0:
                    residual = residual + i+1 - non_shy #TODO: ????
                    non_shy += si[i+1] + (i+1 - non_shy)
        print "Case #" + str(index) + ": " + str(residual)
        g.write("Case #" + str(index) + ": " + str(residual)+"\n")
            
    
    

turn = int(f.readline())
for index in range(1, turn+1):
    line = f.readline().split()
    smax = int(line[0])
    si = []
    for i in line[1]:
        si.append(int(i))
    solve(int(index), smax, si)
