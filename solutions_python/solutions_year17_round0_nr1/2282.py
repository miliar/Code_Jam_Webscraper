def flip_section(i, k, p_list):
    for j in range(i, i+k):
        if p_list[j] == '+':
            p_list[j] = '-'
        else:
            p_list[j] = '+'

def solve(line):
    comps = line.split()
    pancakes_str = comps[0]
    k = int(comps[1])
    n = len(pancakes_str)
    p_list = list(pancakes_str)
    
    flips = 0
    
    for i in range(n-k+1):
        #print("i = ", i)
        #print(p_list)
        if p_list[i] == '-':
            #print("yes")
            flip_section(i, k, p_list)
            flips += 1
    
    
    
    # check success / failure
    if '-' in p_list:
        return "IMPOSSIBLE"
    else:
        return str(flips)


def main():
    infile = open('A-large.in')
    n = int(infile.readline())
    outfile = open('A_mytest.out', 'w')
    for i in range(1, n+1):
        line = infile.readline().strip()
        sol = solve(line)
        outfile.write("Case #{}: {}".format(i, sol) + '\n')

main()