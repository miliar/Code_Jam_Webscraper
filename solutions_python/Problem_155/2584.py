#!/usr/bin/python

import sys

def main():
    f = open(sys.argv[1], 'r')
    Input = f.readlines()
    T = int(Input[0])
    output = []
    for i in range(1, T+1):
        case = Input[i].split(' ')
        s_max = int(case[0])
        string = case[1]
        min_num_frnd = 0
        num_of_audience = 0
        for j in range(s_max + 1):
            if num_of_audience < j:
                frnd = j - num_of_audience
                num_of_audience += frnd
                min_num_frnd += frnd
            num_of_audience += int(string[j])
        output.append("Case #" + str(i) + ": " + str(min_num_frnd) + '\n')
    f2 = open('output.txt','w')
    f2.writelines(output)

if __name__ == "__main__":
    main()
