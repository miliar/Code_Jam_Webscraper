# -*- coding:utf-8 -*-
import os
basepath = '/Users/voidus/Documents/workspace/xp/jam/files/dance'

srcfilename = os.path.join(basepath, 'B-large.in')
dstfilename = os.path.join(basepath, 'B-large.out.txt')

def solve(N, surprising, threshold, numbers):
    result = 0
    numbers = sorted(numbers, reverse=True)
    greater = [number for number in numbers if number // 3 >= threshold]
    lower = [number for number in numbers if number // 3 < threshold]
    result += len(greater)
    for number in lower:
        div = number // 3
        mod = number % 3
        if mod in (1, 2) and div+1 >= threshold:
            result += 1
            continue
        if surprising > 0:
            if mod == 2:
                if div+2 >= threshold:
                    result += 1
                    surprising -= 1
                    continue
            elif div > 0:
                if div+1 >= threshold:
                    result += 1
                    surprising -= 1 
    return result

if __name__ == '__main__':
    with open(srcfilename, 'rb') as inp:
        with open(dstfilename, 'wb') as outp:
            lines = inp.readlines()
            count = int(lines.pop(0))
            outlines = []
            for i in xrange(count):
                line = lines[i].translate(None, '\r\n')
                numbers = [int(number) for number in line.split(' ')]
                N = numbers[0]
                S = numbers[1]
                p = numbers[2]
                result = solve(N, S, p, numbers[3:])
                outlines.append('Case #%d: %d\n' % (i+1, result))
            outp.writelines(outlines)
