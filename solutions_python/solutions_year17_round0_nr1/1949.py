#!/usr/bin/env python
import argparse
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input","-i", help="input file")
    parser.add_argument("--output","-o")
    args = parser.parse_args()
    return args
def pancake(pancakes,K):
    size = len(pancakes)
    # store tehe info from the k last idnex
    # the pancake is in reverse now
    # find the first -
    i    = 0
    found = False
    while i <= size -1:
        if pancakes[i] == "-":
            found = True
            flip = 0
            break
        i+=1
    if not found:
        return 0
    # found at least 1 "-" at index i
    my_list = [-1 if item == "-" else 1 for item in pancakes[i:]]
    j = 0
    #print (my_list)
    while j <= size - K - 1 - i:
        if my_list[j] == -1:
            flip +=1
            for index in range(1,K):
                my_list[j+index] = my_list[j+index] *(-1)
        j+=1
        if j == size - K - i:
            break
    # deal with the rest of K-1
    #print (my_list)
    if (size - K - i) <0:
        return "IMPOSSIBLE"
    for index in range(size - K - i,size-i-1):
        if my_list[index] != my_list[index+1]:
            return "IMPOSSIBLE"
    if my_list[index] == -1:
        flip +=1
    return flip
if __name__ == "__main__":
    arguments = get_arguments()
    output    = arguments.output
    input     = arguments.input
    infile    = open(input,"r")
    outfile   = open(output,"w")
    test      = int(infile.readline().strip())
    for i in range(1,test+1):
        pancakes,K = infile.readline().strip().split(' ')
        print (i)
        print (pancakes,K)
        outfile.write("Case #{}: {}\n".format(i,pancake(pancakes,int(K))))
    infile.close()
    outfile.close()
    

