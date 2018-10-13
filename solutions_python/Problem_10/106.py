#!/usr/bin/python
# Google Code Jam 2008

def solve(P, K, L, freq):
    #print P, K, L, freq
    freq.sort()
    freq.reverse()
    presses = 0
    alpha = 0
    button = 0
    while alpha < L:
        button = button % P
        for i in range(K):
            #print  (button+1), freq[alpha]
            presses = presses  + ((button+1) * freq[alpha])
            alpha += 1  
            if alpha >= L:
                break
        button += 1
        
    return presses

def parse_test(data):
    line = 0
    [P, K, L] = [int(num) for num in data[line].split(" ")]
    line += 1
    freq = [int(num) for num in data[line].split(" ")]
    line += 1
    return (line, [P, K, L, freq]) 

def main():
    import sys
    filename = sys.argv[1]
    input = open(filename)
    data = [line.strip() for line in input.readlines()]
    num_testcases = int(data[0])
    line = 1
    for i in range(1, num_testcases+1):
        (lines, test) = parse_test(data[line:])
    #    print test
        answer = apply(solve, test)
        print "Case #%d: %d" % (i, answer)
        line = line + lines
    input.close()

if __name__ == "__main__":
    main()


