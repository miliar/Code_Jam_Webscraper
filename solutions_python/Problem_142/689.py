from collections import Counter
def main():
    f=open('/home/ayush/A-small-attempt0.in','r')
    o = open("/home/ayush/Downloads/output.txt",'w')
    t=int(f.readline())
    x=0
    while t:
        t-=1
        x+=1
        n=int(f.readline())
        s=[]
        for i in range(n):
            s.append(f.readline())
        moves = 0
        while(s[0]!=''):
            counter = [0]*n
            j=0;flag=1
            char = s[0][0]
            for st in range(n):
                i=1
                if s[st] != '' and s[st][0] != char:
                    flag=0
                    break
                while(i<len(s[st]) and s[st][i] == s[st][0] == char):
                    i+=1
                s[st] = s[st][i:]
                counter[j]=i
                j+=1
            if flag==0:
                break
            data = Counter(counter)
            freq = data.most_common(1)[0][1]
            possmode =[]
            minterm = data.most_common(1)[0][0]
            for tup in data.most_common():
                if freq==tup[1]:
                    possmode.append(tup[0])
                elif freq<tup:
                    break
            possmode.sort()
            mode = possmode[len(possmode)/2]
            for c in counter:
                moves += abs(c-mode)
        if (s[1]==''):
            o.write('Case #%d: %d\n' %(x,moves))
        elif flag==0:
            o.write('Case #%d: Fegla Won\n' %(x))
            
        
main()
        
