#import numpy
import math

def parse():
    f = open('fas_small.txt', 'r+')
    f2 = open('fas_small_out.txt', 'r+')
    
    rounds = int(f.readline())
    
    for i in range(rounds):
        line = f.readline().split(" ")
        line = (int(line[0]), int(line[1]))
        print ("Case #" + str(i+1) + ": " + str(countthem(line[0], line[1])))
        f2.write("Case #" + str(i+1) + ": " + str(countthem(line[0], line[1])) + '\n')
    f.close()
    f2.close()

def reverse(number):
    return int(str(number)[::-1])

def generate():
    for i in range(1000):
        if (i == reverse(i)) & ((round(math.sqrt(i)))**2 == i) & (round(math.sqrt(i)) == reverse(round(math.sqrt(i)))):
            print (i)
        
def countthem(start, end):
    count = 0
    for i in range(start, end+1):
        if (i == reverse(i)) & ((round(math.sqrt(i)))**2 == i) & (round(math.sqrt(i)) == reverse(round(math.sqrt(i)))):
            count += 1
    return count
