import sys

flip_counter = 0
sys.setrecursionlimit(2000)
def check_flips(s,k):
    global flip_counter
    # print (s)
    if len(s)==k:
        # print ('reached')
        if '-' in s and '+' in s:
            flip_counter = 'IMPOSSIBLE'
        elif '-' in s:
            flip_counter += 1
        # print('Counter: ',flip_counter)
        return
    # for i in range(0,len(s)-k-1):
    if s[0]=='-':
        s=flip(s,k)
        flip_counter += 1
        check_flips(s[1:],k)
    else:
        check_flips(s[1:],k)


def flip (s,k):
    sw = lambda x: '+' if x=='-' else '-'
    for i in range(0,k):
        s[i]=sw(s[i])
    return s

input = open('gs1.txt', 'r')
tests = int(input.readline())
# print (tests)
for i in range(1,tests+1):
    test = input.readline()
    (s,k) = test.split(' ')
    # print (s,k)
    s = list(s)
    k = int(k)
    flip_counter = 0
    check_flips(s,k)
    print ('Case #%s:'%i,flip_counter)
    # print ()
