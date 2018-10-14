import sys
googlerese={'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', ' ':' '}
temp=sys.stdin
testcase = open('a-small.in','r')
sys.stdin = testcase
solution = open('a-small.out','w')
t = int(input())
for i in range(t):
    g = input()
    s=''.join([googlerese[i] for i in g])
    print('Case #' + str(i+1) + ': ' + s, file=solution)
solution.close()
testcase.close()
sys.stdin=temp
