"""
	Filename:  password.py
	Author:    Jason Cramer
	Google Code Jam Round 1 Problem A Solution

"""
import sys


def product(a, probs):
    result = 1
    for i in range(a):
        result = result * probs[i]
    return result

def option1(a, b, probs):
    c = product(a, probs)
    e_c = c*(b - a + 1)
    e_i = (1-c)*(2 * b - a + 2)
    return e_c + e_i

def option2(a, b, probs):
    minim = float('inf')
    for s in range(1,a+1):
        c = product(a - s, probs)
        e_c = c*float(2*s + b - a + 1)
        e_i = (1-c)*float(2*s + 2 * b - a + 2)
        if e_c + e_i < minim:
            minim = e_c + e_i
    return float(minim)

def option3(a, b, probs):
    return float(2 + b)

def weighoptions(nums, probs):
    nums = list(map(int, nums))
    probs = list(map(float, probs))
    a = nums[0]
    b = nums[1]
    return min(option1(a, b, probs), option2(a, b, probs), option3(a, b, probs))


def main():
    args = sys.argv[1:]
    f = open('output_password.txt', '+w')
    for i in range(int(input())):
        f.write('Case #' + str(i + 1) + ': ' + str(weighoptions(input().split(), input().split())) + '\n')

if __name__ == '__main__':
    sys.exit(main())

