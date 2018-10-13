__author__ = 'asus'
import math


def palindrome(x):
    s = str(x)
    for i in range(len(s)/2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

fin = open("input.txt", 'r')
fout = open("output.txt", 'w')

n = int(fin.readline())

for i in range(n):
     interv = fin.readline().split(" ")
     a = int(interv[0])
     b = int(interv[1])
     count = 0
     for j in range(a, b + 1):
         if palindrome(j) and (math.trunc(math.sqrt(j)) == math.sqrt(j)) and palindrome(math.trunc(math.sqrt(j))):
             count += 1
     fout.write("Case #" + str(i + 1) + ": " + str(count) + "\n")

fin.close()
fout.close()