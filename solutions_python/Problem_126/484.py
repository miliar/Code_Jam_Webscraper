'''
Created on May 12, 2013

@author: grayfox
'''

vocals = ('a','e','i','o','u')

def get_con_groups(s,n):
    res = []
    start = -1
    for i in range(len(s)):
        if start == -1 and s[i] not in vocals:
            start = i
        if start != -1 and s[i] in vocals:
            if i-start >= n:
                res.append((start,i-1))
            start = -1
    if start != -1 and len(s) - start >= n:
        res.append((start,len(s)-1))
    return res

def solve(s,n):
    count = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            groups = get_con_groups(s[i:j+1],n)
            if len(groups) > 0:
                count += 1
    return count

if __name__ == '__main__':
    f = open("testcase")
    lines = int(f.readline())
    for i in range(lines):
        case = f.readline().split()
        print("Case #%s: %s" % (i+1,solve(case[0],int(case[1]))))
        