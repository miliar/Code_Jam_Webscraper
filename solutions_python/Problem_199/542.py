# Problem A - Pancakes
import random

def openfile(filename, separator = False):
    # Open the .in file specified by filename as a string 
    # Split it into a list (using the separator if specified)
    # Return that list    
    string = open(filename).read()
    if separator == False: return string.split()
    return string.split(separator)

input_filename = 'A-large.in'
output_filename = 'A-large-output1.in'

def main(input_filename, output_filename):
    
    lis = openfile(input_filename)
    output_file = open(output_filename,'w')
    
    for i in range(1,int(lis[0])+1):
        s = lis[2*i-1]
        k = int(lis[2*i])
        res = flipfromleft(s,k)
        text = 'Case #{}: {}\n'.format(i, res)
        output_file.write(str(text))

# MAINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
s = '---------------'


def flip(s,k,ind):
    # s = '+--+--++---+++'
    # k = 5 <= len(s)
    # ind = 2 where 0 <= ind <= len(s)-k
    if k > len(s) or ind<0 or ind>len(s)-k: return s
    res = s[:ind]
    for i in range(ind,ind+k):
        if s[i] == '+': res += '-'
        if s[i] == '-': res += '+'
    res += s[ind+k:]
    #print(s)
    return res

def strip(s):
    while s[0] == '+' or s[-1] == '+':
        s = s.strip('+')
    return s

def flipfromleft(s,k,i=0):
    if k > len(s): return 'IMPOSSIBLE'
    if '-' not in s: return i
    s = strip(s)
    s = flip(s,k,0)
    return flipfromleft(s,k,i+1)
