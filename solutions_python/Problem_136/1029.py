#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    in_file = open("B-large.in", mode='r')
    out_file = open("B-large.out", mode='w')

    T = int(in_file.readline())
    
    for i in range(T):
        C, F, X = [float(x) for x in in_file.readline().strip().split()]
        total = 0.0
        base = 2 
        N = 0

        while (X/(base+N*F)) > (C/(base+N*F)) + (X/(base+(N+1)*F)):
            total += (C/(base+N*F))
            N += 1
        total += (X/(base+N*F))

        out_file.write("Case #" + str(i+1) + ": " + "{:.7f}".format(total) + "\n") 

    in_file.close()
    out_file.close()

if __name__ == '__main__':
    main()