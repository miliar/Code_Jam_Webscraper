import string
import array


def isPalindrome(s):
    s = str(s)
    n = len(s)
    for i in range(len(s)):
        if s[i] != s[n-i-1]:
            return False
    return True


palindromes = []

for i in range(10000010):
    k = i * i
    if isPalindrome(k) and isPalindrome(i):
        #print i, k
        palindromes.append(k)

print palindromes

in_file = r'D:\python\a.txt'
out_file = r'D:\python\b.txt'

file_in = open(in_file, 'r')
file_out = open(out_file, 'w')

T = int(file_in.readline())
count = 0
for i in range(T):
    count+=1
    line = file_in.readline()
    A = line.split()
    a, b = long(A[0]), long(A[1])
    num = 0
    for j in palindromes:
        if j >= a and j <= b:
            num += 1
    #print 'Case #' + str(count) + ': ' + str(num)
    file_out.write('Case #' + str(count) + ': ' + str(num) + '\n')

file_out.close()
    
