import os
import math

INFILE = r'C:\Users\noam\workspace\CodeJam\input.txt'
def parse_lines(line):
    words = list(x for x in line.split() if x)
    return words

def res_to_str(res):
    return str(res)

def solve(low, high):
    sqrt_low = math.sqrt(low)
    if math.modf(sqrt_low)[0] != 0:
        sqrt_low = math.ceil(sqrt_low)
    sqrt_low = int(sqrt_low)
     
    sqrt_high = math.sqrt(high)
    if math.modf(sqrt_high)[0] != 0:
        sqrt_high = math.floor(sqrt_high)
    sqrt_high = int(sqrt_high)
    
    counter = 0
    for x in xrange(sqrt_low, sqrt_high + 1):
        x_str = str(x)
        if x_str != x_str[::-1]:
            continue
        
        s = str(x**2)
        if s == s[::-1]:
            counter += 1 
            
    return counter
    
    

def main():
    infile = file(INFILE)
    outfile = file(INFILE + '.result.txt', 'wt')
    test_cases = infile.readline()
    num = int(test_cases)
    for case in xrange(num):
        low, high = (int(x) for x in infile.readline().split())
        res = solve(low, high)
        str_res = res_to_str(res)
        res_line = 'Case #%d: %s\n' % (case+1, str_res)
        print res_line,
        outfile.write(res_line)
    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()

