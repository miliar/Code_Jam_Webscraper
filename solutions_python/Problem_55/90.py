def solve(R, k, N, g):
    pos = 0
    result = 0
    prev = { }
    while R > 0:
        s = 0
        start = pos
        while s + g[pos] <= k:
            s += g[pos]
            pos = (pos + 1) % N
            if pos == start:
                break
        R -= 1
        result += s
        if pos in prev.keys():
            rr, res = prev[pos]
            rides = rr - R
            result += (result - res) * (R / rides)
            R = R % rides
        else:
            prev[pos] = (R, result)
    return result
    
def main():
    file = open('C-large.in')
    output = open('output.txt', 'w')
    tests = int(file.readline().strip())
    for case in range(1, tests + 1):
        R, k, N = [int(x) for x in file.readline().split()]
        g = [int(x) for x in file.readline().split()]
        print >> output, 'Case #%d:' % case, solve(R, k, N, g)
    output.close()
    
if __name__ == '__main__':
    main()
    
