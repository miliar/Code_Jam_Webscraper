d={'\n':'\n',' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
f=open('a.txt','r')
out=open('out.txt','w')
result=[]
for linenum,line in enumerate(f):
    if linenum==0:
        continue
    s=''
    for i,ch in enumerate(line):
        s=s+d[ch]
    s="Case #%d: "%linenum +s
    result.append(s)
out.writelines(result)
out.close()
f.close()

    
