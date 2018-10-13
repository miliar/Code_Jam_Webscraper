def solve(string,i,n):

    for j in range(i,i+n):
        if string[j]=='-':
            string[j]='+'
        else:
            string[j]='-'




for a0 in range(int(input())):
    string,k=input().split(' ')
    k=int(k)
    count=0
    string=list(string)

    for i in range(len(string)-k+1):
        if string[i]=='+':
            continue
        count += 1
        solve(string,i,k)


    c=string.count('-')
    if c > 0:
        print('Case #{0}: IMPOSSIBLE'.format(a0+1))
    else:
        print("Case #{0}: {1}".format(a0+1, count))

