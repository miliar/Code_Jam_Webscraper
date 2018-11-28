def tidy(s):
    N = int(s)
    S = list(s)[:-1]
    # verify if it isn't already tidy:
    flag=True
    if len(S)==1:
        return `N`
    print S
    for i in range(0,len(S)-1):
        if int(S[i+1])<int(S[i]):
            flag=False
            first = i #first digit which is breaking the "tidiness"
            break
    if flag:
        return `int(''.join(S))`
    # set digits after `first` to be 9:
    for i in range(first+1,len(S)):
        S[i]='9'
    S[first]=str(int(S[first])-1)
    print first

    # get largest number, by decreasing S step by step
    # we need `first` steps to be sure, but also take into consideration the fact that S[0] may be 1->0 and we won't write it
    for i in range(first,0,-1):
        if (int(S[i]) < int(S[i-1])) or S[i]=='0': # we can't just decrease by 1 digit:
            S[i]='9'
            S[i-1]=str(int(S[i-1])-1)
    print S
    return `int(''.join(S))`

f = open('input.in', 'r')
T = int(f.readline())
tcs = []

for i in range(T):
    tcs.append(f.readline())

f.close()
f = open('output.txt', 'w')
for i in range(T):
    f.write("Case #%s: %s\n" % (i+1, tidy(tcs[i])))
f.close()

