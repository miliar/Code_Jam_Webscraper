# Repeater

import sys
import math

def diff(arr1, arr2):
    n = len(arr1)
    actions = 0
    for i in range(0,n):
        actions += math.fabs(arr1[i] - arr2[i])   
    return(actions)


def base_diff(string):
    lenstr = len(string)
    retarr = []
    cl = string[0]
    ct = 1
    for i in range(1,lenstr):
        if string[i] == cl:
            ct += 1
        else:
            retarr += [ct]
            ct = 1
            cl = string[i]
    retarr += [ct]
    return(retarr)

# Find base (minimum) string
def calc_base(string):
    base = ""
    base += string[0]
    last_letter = string[0]
    for l in range(1,len(string)):
        if string[l] != last_letter:
            base += string[l]
            last_letter = string[l]
    return(base)
            
def possible(strings, N):
    base = calc_base(strings[0])
    for i in range(1,N):
        new_base = calc_base(strings[i])
        if new_base != base:
            return(False)
        

def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')

    line = infile.readline()
    T = int(line)

    for t in range(1,T+1):
        line = infile.readline()
        N = int(line)
        strings = []
        for i in range(0,N):
            line = infile.readline().strip("\n")
            strings += [line]

        if possible(strings, N) == False:
            outfile.write("Case #{0}: Fegla Won\n".format(t))
        else:
            if(N==2):
                arr1 = base_diff(strings[0])
                arr2 = base_diff(strings[1])
                actions = int(diff(arr1,arr2))
                print(actions)
                outfile.write("Case #{0}: {1}\n".format(t, int(actions)))    
        
    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()
