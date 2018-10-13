#!/usr/bin/env python
import sys

def main(in_array):
    results = []
    for i in in_array:
        val = reduce(lambda x, y: x^y, i[1:])
        if val == 0:
            sum = 0
            min = i[1]
            sum += min
            for j in xrange(2, i[0]+1):
                if i[j] < min:
                    min = i[j]
                sum += i[j]
            results.append((sum - min))
        else:
            results.append('NO')
    return results

if __name__ == "__main__":
    in_array = []
    infile = open('C-large.in', 'rU')
    outfile = open('out', 'w')
    inputs = int(infile.readline())
    for i in xrange(0,inputs):
        in_array.append([])
        in_array[i].append(int(infile.readline()))
        input = map(lambda x: int(x), infile.readline().split())
        in_array[i].extend(input)
    infile.close()

    results = main(in_array)

    for result in xrange(0, inputs):
        outfile.write(("Case #%d: %s\n") % (result+1, str(results[result])))
    outfile.close()
