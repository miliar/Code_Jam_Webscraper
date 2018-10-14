def mul(a,b):
    if a==b :
        return -1

    elif a=='1' :
        return b
    elif a=='-1' :
        return '-'+b
    elif a=='i' and b=='j' :
        return 'k'
    elif a=='i' and b=='k' :
        return '-j'
    elif a=='j' and b=='k' :
        return 'i'
    elif a=='j' and b=='i' :
        return '-k'
    elif a=='k' and b=='i' :
        return 'j'
    elif a=='k' and b=='j' :
        return '-i'

    elif a=='-i' and b=='j' :
        return '-k'
    elif a=='-i' and b=='k' :
        return 'j'
    elif a=='-j' and b=='k' :
        return '-i'
    elif a=='-j' and b=='i' :
        return 'k'
    elif a=='-k' and b=='i' :
        return '-j'
    elif a=='-k' and b=='j' :
        return 'i'

    elif a=='-i' and b=='-j' :
        return 'k'
    elif a=='-i' and b=='-k' :
        return '-j'
    elif a=='-j' and b=='-k' :
        return 'i'
    elif a=='-j' and b=='-i' :
        return '-k'
    elif a=='-k' and b=='-i' :
        return 'j'
    elif a=='-k' and b=='-j' :
        return '-i'

    elif a=='i' and b=='-j' :
        return '-k'
    elif a=='i' and b=='-k' :
        return 'j'
    elif a=='j' and b=='-k' :
        return '-i'
    elif a=='j' and b=='-i' :
        return 'k'
    elif a=='k' and b=='-i' :
        return '-j'
    elif a=='k' and b=='-j' :
        return 'i'

    elif a=='-k' and b=='k' :
        return '-k'
    elif a=='-i' and b=='i' :
        return '-i'
    elif a=='-j' and b=='j' :
        return 'j'


if __name__=="__main__":
    #k='-1'
    #print mul(k,'j')
    w = open('C:/Users/rajiv/Desktop/code jam 15/C-small-attempt0.out', 'w')
    lines = [line.strip() for line in open('C:/Users/rajiv/Desktop/code jam 15/C-small-attempt0.in')]
    for i in range(1,2*(int(lines[0]))+1,2):
            p=list(lines[i].split())
            p=map(int,p)
            i=i+1
            l=list(lines[i])
            #print p
            l=l*p[1]
            #print l
            c='1'
            s=0
            t=0
            f=0
            for j in range(0,l.__len__()):
                r=mul(c,l[j]).__str__()
                #print c.__str__()+' '

                #print 'mul('+c.__str__()+','+l[j].__str__()+') ='+r.__str__()
                c=r
                if r=='i' and f==0 :
                    f=1
                    c='1'
                if f==1 and s==0 and r=='j' :
                    s=1
                    c='1'
                if s==1 and t==0 and r=='k' and j==l.__len__()-1:
                    t=1
                    break
            #print j
            #print l.__len__()
            if t==1 :
                print 'Case #'+int((i/2)).__str__()+': YES'
                w.write('Case #'+int((i/2)).__str__()+': YES' + '\n')
            else :
                print 'Case #'+int((i/2)).__str__()+': NO'
                w.write('Case #'+int((i/2)).__str__()+': NO' + '\n')





    #print 'Case #' + int((i/2)).__str__() + ': ' + min_time.__str__()
    #f.write('Case #' + int((i/2)).__str__() + ': ' + min_time.__str__() + '\n')

#f.close()
