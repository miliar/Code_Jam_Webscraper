r = open('C-small-attempt1.in')
f = open('C.out', 'w')
T = int(r.readline())

i = 1
fair = [1,4,9,121,484]
while i <= T:
    t_out = 'Case #'+str(i)+': '
    i += 1
    ab = r.readline().split()
    a = int(ab[0])
    b = int(ab[1])
    count = 0
    for n in fair:
        if n >= a and b >= n:
            count += 1
    t_out += str(count)
    f.write(t_out)
    f.write('\n')

def isPalindrome(n):
    n = str(n)
    for i in range(len(n)):
        if not n[i] == n[len(n)-i]:
            return False
    return True
