import sys

def Solve(s,k):
    tm = '-'*k
    tp = '+'*k
    count = 0
    sub = ''
    count+=s.count(tm)
    s = s.replace(tm,tp)
    for i in range(len(s)):
        if (s[i]=='-') and i<=(len(s)-k):
            count +=1
            for j in range(k):
                if (s[j+i]=='-'):
                    sub += '+'
                else:
                    sub += '-'
            if i==0:
                temp_s = ''
            else:
                temp_s = s[:i]
            s = temp_s + sub + s[i+k:]
        sub=''
        if i==len(s)-1 and ('-' in s):
            return "IMPOSSIBLE"
    return count
    

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  S,K = raw_input().split()
  s = Solve(S, int(K))
  print "Case #{}: {}".format(i, s)

   
