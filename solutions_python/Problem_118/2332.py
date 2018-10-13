# -*- coding: utf-8 -*-
import math

INPUT = 'C-small-attempt0.in'
OUTPUT = 'output-c-small.txt'


def result(caseno, msg):
    output = open(OUTPUT, 'a')
    output.write('Case #%d: %s\n' % (caseno, msg))
    output.close()

def main():
    input = open(INPUT, 'r')

    caseno = 0
    data = []
    input.readline()    # 1行目は無視
    for line in input:
        count = 0
        line = line.replace('\n', '')
        data = line.split(' ')
        if len(data) == 2:
            start = int(data[0])
            end = int(data[1])
            for num in range(start, end+1):
                isfair = False
                x = math.sqrt(num)
                if x == int(x): # 平方数か
                    if num < 10:
                        isfair = True

                    str1 = '%d' % int(x)
                    str2 = '%d' % num
                    if str1 == str1[::-1] and str2 == str2[::-1]:
                        isfair = True 

                if isfair:
                    count += 1

        caseno += 1
        result(caseno, count)

    input.close()


if __name__ == '__main__':
    main()
