#!/usr/bin/python
from sys import argv


def calculate_candies(n_candies, weight):
    res = weight[0]
    for x in weight[1:]:
        res = res ^ x
    if res != 0:
        return 'NO'
    else:
        return sum(weight)-min(weight)


def candy(input_file, output_file):
    f=open(input_file, 'r')
    N=int(f.readline())
    g=open(output_file, 'w')
    for i in xrange(N):
        n_candies=int(f.readline())
        line=f.readline()
        weight=[]
        for x in line.split(' '):
            weight.append(int(x))
        g.write('Case #'+str(i+1)+': ')
        candies=calculate_candies(n_candies, weight)
        g.write(str(candies)+'\n')
    f.close()
    g.close()


#run: python candy.py input output
if __name__=='__main__':
    if argv[0].find('candy.py')!=-1:
        if len(argv)>=3:
            candy(argv[1], argv[2])
