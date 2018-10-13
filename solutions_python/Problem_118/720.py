def is_palindrome(s):
    l = len(s)
    for i in range(0, l/2):
        if s[i] != s[l-1-i]:
            return 0
    return 1

def find_palindrome():
    n = 1
    i = 1

    while (i < 10000000000):
        n += 2 * i + 1
        i += 1
        if (is_palindrome(str(i)) and is_palindrome(str(n))):
            print i;

#find_palindrome()

file=open("a.dat")
l = []

while 1:
    line=file.readline()
    if not line:
        break;
    a=int(line)
    l.append(a**2)

f = open("C-large-1.in")
n = int(f.readline())
for i in range(0, n):
    line=f.readline().split(" ")
    a = int(line[0])
    b = int(line[1])
    s=-1
    t=-1
    for u in range(0, len(l)):
        if s < 0 and l[u] >= a:
            s=u
        if s >= 0 and l[u] > b:
            t=u
            break
    if s== -1 or t == -1:
        print "error"
    print "Case #"+str(i+1)+": " + str(t-s)
