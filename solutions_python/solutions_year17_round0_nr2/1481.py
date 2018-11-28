def Solve_large(n):
    a = [d for d in str(n)]
    temp=0
    if str(n)==''.join(sorted(str(n))):
        return n
    else:
        for i in range(len(a)-1,0,-1):
            if a[i]<a[i-1]:
                for j in range(i,len(a)):
                    a[j]='9'
                a[i-1] = str(int(a[i-1])-1)
            if a[0]=='0':
                a = a[1:]
    return int(''.join(a))                
    

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  N = input()
  s = Solve_large(N)
  print "Case #{}: {}".format(i, s)
