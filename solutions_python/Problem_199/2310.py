import sys


def flip(string,i,k):
    for j in range(i,i+k):
        if string[j]=='-':
            string=string[:j]+'+'+string[j+1:]
        else:
            string=string[:j]+'-'+string[j+1:]
    return string



for tc in range(int(raw_input())):
    string,k = raw_input().split()
    k = int(k)
    minus = 0
    plus = 0

    for i in string:
        if i=='-':
            minus += 1
        else:
            plus += 1
    
    cnt = 0
    for i in range(len(string)-k+1):
        if string[i]=='-':
            string = flip(string,i,k)
            cnt += 1
    if string.count('-')==0:
        print "Case #"+str(tc+1)+": "+str(cnt)

    else:
        print "Case #"+str(tc+1)+": IMPOSSIBLE"
