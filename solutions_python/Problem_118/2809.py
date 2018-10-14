import math
def is_square(integer):
    root = math.sqrt(integer)
    if int(root) ** 2 == integer:
        return root
    else:
        return False

def is_palindrome(number):
    number = str(number)
    return number == number[::-1]

test_list = []
tmin,tmax = 1000L,0L
with open('input.txt','r') as inf:
    n = int(inf.readline().strip())
    for t in range(n):
        a,b = inf.readline().strip().split()
        a,b = long(a), long(b)
        test_list.append((a,b))
        if tmin>a:
            tmin=a
        if tmax<b:
            tmax=b
print tmin,tmax
fair_square = []
i = tmin
while i<tmax:
    ii = is_square(i)
    if ii:
        if is_palindrome(i) and is_palindrome(long(ii)):
            fair_square.append(i)
    i+=1

with open('output.txt','w') as ouf:
    t = 0
    for a,b in test_list:
        t += 1
        i = 0
        count = 0
        try:
            while fair_square[i] < a:
                i+=1
            while fair_square[i] <= b:
                count+=1
                i+=1
        except IndexError:
            pass

        ouf.write('Case #%i: %s\n'%(t,count))

