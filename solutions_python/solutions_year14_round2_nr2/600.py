# __author__ = 'yurychebiryak'

def solve (A, B, K):
    ways = 0
    for a in range(A):
        for b in range(B):
            if a & b < K:
                ways+=1
    return ways

def run(input, output):
    file = open(input, 'r')
    out = open(output, 'w')
    lines = file.readlines()
    for i in range(int(lines[0].strip())):
        [A, B, K] = [ int(x) for x in lines[i + 1].split(" ") ]
        ways = solve(A, B, K)
        out.write("Case #%d: %d\n" % (i+1, ways) )
        print("Case #%d: %d\n" % (i+1, ways) )

run("example", "exampleOut.txt")
run("small.txt", "smallOut.txt")