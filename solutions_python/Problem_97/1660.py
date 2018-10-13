def process_file(file):
    fsock = open(file)
    text = fsock.read()
    fsock.close()
    lines = text.split('\n')
    return lines


def check(n, m):
    recycled = 0
    for i in range(1, len(n)):
        z = n[len(n)-i:] + n[:len(n)-i]
        if z == m:
            #print z, m
            recycled += 1
    return recycled


# define our method
def solve(line):
    a = int(line.split(" ")[0])
    b = int(line.split(" ")[1])
    result = 0
    for n in range(a, b):
        m = b
        while m > n:
            result += check(str(n), str(m))
            m -= 1
    return result

    
def process_lines(lines):
    ans = []
    for cur in range(1, len(lines)-1):
        ans.append(solve(lines[cur]))
    return ans


if __name__ == "__main__":
    import sys, re, string
    filename = sys.argv[1]
    lines = process_file(filename)
    inp = process_lines(lines)
    for k, v in enumerate(inp):
        print "Case #%d: %s" % (k + 1, v)
