def recur(s):
    if len(s)<=1:
        return s
    if s[-2]<=s[-1]:
        return recur(s[:-1]) + str(s[-1])
    else:
        new = s[:-2] + str(int(s[-2])-1)
        return recur(new)+"9"
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n= raw_input()
    tidy = recur(n)
    tidy = str(int(tidy))
    superTidy = tidy
    try:
        last9 = tidy.index('9')
        superTidy = tidy[:last9]+('9'*(len(tidy)-last9))
    except Exception as e:
        superTidy=tidy
    if int(superTidy)<=int(n):
        print "Case #" +str(i)+": " + str(superTidy)
    else:
        print "Case #" +str(i)+": " + tidy
