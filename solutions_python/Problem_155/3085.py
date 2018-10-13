'''
Created on Apr 11, 2015

@author: owner
'''
import sys

def main(args):
    f = open(args[1],'r')
    num_tests = f.readline()
    outfile = open('C:\Users\owner\workspaces\BIA656HW\Goodreads\src\output.txt', 'w')
    counter = 1
    for line in f:
        s_max = line.split(' ')[0]
        s = line.split(' ')[1].strip()
        outfile.write('Case #' + str(counter) + ': ' + solve(s_max, s) +'\n')
        counter +=1
    f.close()

def solve(s_max, s):
    #s_max = 0
    #s = '1'
    needed = 0
    num_people = 0
    for idx,item in enumerate(s):
        if idx == 0:
            num_people += int(item)
        else:
            if idx > num_people+needed:
                needed += idx - (num_people+needed)
            num_people += int(item)
    return str(needed)
    #needed += item - cumsum(s[0,idx])

if __name__ == '__main__':
    main(sys.argv)