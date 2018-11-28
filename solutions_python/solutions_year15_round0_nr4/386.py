
def parse(input_file, output_file):
    with open(input_file) as f:
        #lines = f.readlines()
        #print(f.readline())
        n_cases = int(f.readline().split()[0])
        data = dict()
        for i in range(n_cases):
            data[i] = [int(x) for x in f.readline().split()]
    f = open(output_file, 'w')
    for i in range(n_cases):
        rich_win = solve(data[i])
        winner = "RICHARD" if rich_win else "GABRIEL"
        line = "Case #"+str(i+1)+": "+str(winner)
        print(line)
        f.write(line+'\n')
    return

def solve(xrc):
    x = xrc[0]
    r = xrc[1]
    c = xrc[2]
    if xrc == [4,4,2] or xrc == [4,2,4]:
        return True
    if x >= 7:
        return True
    if x > r and x > c:  # can't even fit one in
        return True
    #L shape
    l_short = (x-1)//2+1
    l_long = x+1-l_short
    if min(r, c) < l_short or max(r,c) < l_long: # can't fit an L shape.
        return True
    if (r*c)%x != 0:  # not divisible by x
        return True
    return False


for r in range(1,5):
    for c in range(1,r+1):
        for x in range(1,5):
            print(x,r,c,solve([x,r,c]))

input_file = 'C-large.in'
input_file = 'C-small-attempt0.in'
output_file = 'Coutput-large.txt'
output_file = 'Coutput0'
parse(input_file, output_file)