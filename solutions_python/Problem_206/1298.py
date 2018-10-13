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
output_filename = 'A-large-out.in'

def main(input_filename, output_filename):
    
    lis = openfile(input_filename)
    output_file = open(output_filename,'w')
    
    T = int(lis[0]) # number of test cases  
    
    ind = 1    
    for testcase in range(1,T+1):
        N = int(lis[ind+1])
        length = 2*N        
        testcase_list = lis[ind:ind+2+length]
        
        ind = ind+2+length 
        res = horses(testcase_list)
        text = 'Case #{}: {}\n'.format(testcase, res)
        output_file.write(str(text))

# MAINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
s = '---------------'
lis = ['100', '2', '80', '100', '70', '10']

def horses(lis):
    # Input [D, N, K1, S1, K2, S2, K3, S3, ... Kn]
    D = int(lis[0])
    N = int(lis[1])
    lis = lis[2:]
    Tmax = 0
    for horse in range(N):
        K = int(lis[2*horse])
        S = int(lis[2*horse+1])
        Tmax = max(Tmax, (D-K)/S)
    
    return D/Tmax
