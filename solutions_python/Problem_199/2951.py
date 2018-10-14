t=int(raw_input().strip())
for i in xrange(t):
    s,k=raw_input().strip().split(' ')
    k=int(k)
    dict_symbols={}
    ans=count=0
    while(count<len(s)):
        if(s[count]=='+'):
            count+=1
            continue
        if(count+k<=len(s)):
            for j in xrange(count,count+k):
                if(s[j]=='-'):
                    s=s[:j]+s[j].replace(s[j],'+')+s[j+1:]
                else:
                    s=s[:j]+s[j].replace(s[j],'-')+s[j+1:]
                try:
                    dict_symbols[s[j]].append(j)
                except:
                    dict_symbols[s[j]]=[]
                    dict_symbols[s[j]].append(j)
            if('-' in dict_symbols):
                count=dict_symbols['-'][0]
            else:
                count+=k
        else:
            count+=k
        dict_symbols.clear()
        ans+=1
    if('-' in s):
        ans='IMPOSSIBLE'
    print "Case #{}: {}".format(i+1,ans)
