#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Finding "fair and square" numbers...

Instead of using a naive approach, I directly searched for a more scalable
way to find the number of fair and square numbers in a specified interval.
Outputing the first fair and square numbers along with their square root
shows the following pattern:

    root          square
       0               0
       1               1
       2               4
       3               9
      11             121
      22             484
     101           10201
     111           12321
     121           14641
     202           40804
     212           44944
    1001         1002001
    1111         1234321
    2002         4008004
   10001       100020001
   10101       102030201
   10201       104060401
   11011       121242121
   11111       123454321
   11211       125686521
   20002       400080004
   20102       404090404
  100001     10000200001
  101101     10221412201
  110011     12102420121
  111111     12345654321
  200002     40000800004
 1000001   1000002000001
 1001001   1002003002001
 1002001   1004006004001
 1010101   1020304030201
 1011101   1022325232201
 1012101   1024348434201
 1100011   1210024200121
 1101011   1212225222121
 1102011   1214428244121
 1110111   1232346432321
 1111111   1234567654321
 2000002   4000008000004
 2001002   4004009004004
10000001 100000020000001
10011001 100220141022001
10100101 102012040210201
10111101 102234363432201
11000011 121000242000121
11011011 121242363242121
11100111 123212464212321
11111111 123456787654321
20000002 400000080000004

It seems that (except for the trivial 1-character palindromes) the roots of the
fair and square numbers follow the following pattern (|.| stands for the number
of digits in what follows):

if |root| is even:
    the roots which yields fair and square numbers are either:
    - beginning and ending with 1, the digits inbetween being every possible
      "palindromic" combination of zeros and ones
    - the number 20(...)02
if |root| is odd:
    the roots which yields fair and square numbers are either:
    - beginning and ending with 1, the digits inbetween being every possible
      "palindromic" combination of zeros and ones
    - beginning and ending with 1, the middle digit being 2, and the total number
      of ones being 4
    - the number 20(...)02
    - the number 20(...)1(...)02

I'm assuming (and hoping!) this pattern verifies itself for all fair and square
numbers, which allows to solve the problem more easily given that:

The number of fair and square numbers with n digits (notice that n is odd) is:

if (n+1)/2 is even:
    2**((n+1)/4-1)+1
if (n+1)/2 is odd:
    2**((n+1)/4)+(n+1)/4+2

We should just care handling the different possible intervals...

"""

input_filename = 'C-small-attempt0.in'
output_filename = 'C-small-attempt0.out'

def count_full_between(i, j):
    result = 0
    for k in range(i, j):
        result += 2**(k+1)+k+3
    return result

def count_fair_and_square(A, B):
    if len(A) % 2 == 0 and len(B) % 2 == 0:
        begin = len(A)/2
        end = len(B)/2
        if begin == end:
            return 0
        else:
            if begin % 2 == 0 and end % 2 == 0:
                return count_full_between(begin/2, end/2)
            elif begin % 2 == 0 and end % 2 == 1:
                return count_full_between(begin/2, int(end/2))+2**(int(end/2))+(int(end/2))+2
            elif begin % 2 == 1 and end % 2 == 0:
                return 2**(int(begin/2))+1+count_full_between(int(begin/2)+1, end/2)
            else:
                return 2**(int(begin/2))+1+count_full_between(int(begin/2)+1, int(end/2))+2**(int(end/2))+(int(end/2))+2
    elif len(A) % 2 == 0 and len(B) % 2 == 1:
        fair_and_squares = construct_fair_and_squares(len(B))
        return sum(i <= int(B) for i in fair_and_squares)+count_fair_and_square(A, B[:-1])
    elif len(A) % 2 == 1 and len(B) % 2 == 0:
        fair_and_squares = construct_fair_and_squares(len(A))
        return sum(i >= int(A) for i in fair_and_squares)+count_fair_and_square(A+'1', B)
    else:
        fair_and_squares_A = construct_fair_and_squares(len(A))
        fair_and_squares_B = construct_fair_and_squares(len(B))
        if len(A) == len(B):
            return sum(int(A) <= i <= int(B) for i in fair_and_squares_A)
        else:
            return sum(int(A) <= i for i in fair_and_squares_A)+sum(i <= int(B) for i in fair_and_squares_B)+count_fair_and_square(A+'1', B[:-1])
    
def construct_fair_and_squares(n):
    if n % 2 != 1:
        return None
    size_of_root = (n+1)/2
    if size_of_root == 1:
        return [1,4,9]
    else:
        # a and b will hold the first half of the palindrome
        a = '1'
        b = '2'
        for i in range(int(size_of_root/2)-1):
            a += '0'
            b += '0'
        partial_roots = [a]
        for i in range(2**(len(a)-1)-1):
            a = bin(int(a, 2)+1)[2:]
            partial_roots.append(a)
        roots = []
        for partial_root in partial_roots:
            if size_of_root % 2 == 0:
                roots.append(partial_root+partial_root[::-1])
            else:
                roots.append(partial_root+'0'+partial_root[::-1])
                roots.append(partial_root+'1'+partial_root[::-1])
                if sum(map(int, partial_root)) == 2:
                    roots.append(partial_root+'2'+partial_root[::-1])
        if size_of_root % 2 == 0:
            roots.append(b+b[::-1])
        else:
            roots.append(b+'0'+b[::-1])
            roots.append(b+'1'+b[::-1])
    return sorted(map(lambda x: int(x)**2, roots))

f = open(input_filename)
lines = f.readlines()
f.close()

no_test_cases = int(lines[0])

f = open(output_filename, 'a')

for i in range(no_test_cases):
    interval = lines[i+1].split()
    f.write('Case #'+str(i+1)+': '+str(count_fair_and_square(interval[0], interval[1]))+'\n')

f.close()
