#!/usr/bin/python
import math

def is_palindrome(x):
    array = list(str(x))
    #print array
    if len(array)%2 != 0:
        del array[len(array)/2]
    mid = len(array)/2
    half1 = array[:mid]
    half2 = array[mid:]
    half2.reverse()
    if half1 == half2:
        return True
    else:
        return False

def is_square_root(x):
    candidate = math.sqrt(x)
    return candidate == int(candidate)

def process(A,B,case):
    count = 0
    for number in range(A,B+1,1):
        #print is_palindrome(number)
        if is_palindrome(number) and is_square_root(number):
            if is_palindrome(int(math.sqrt(number))):
                count = count+1
    print "Case #%i: %i" %(case, count)


def input():
  T = int(raw_input())
  for i in range(1,T+1,1):
    x = raw_input()
    x = x.split()
    process(int(x[0]), int(x[1]), i)

def main():
    input()
if __name__ == '__main__':
    main()
