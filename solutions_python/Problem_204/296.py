from os.path import expanduser
import math

problem = "B-small-attempt2"
path = expanduser('C:/Users/SWAPNIL/Downloads/')
file_in = path + problem + '.in'
file_out = path + problem + '.out'
      
with open(file_in,'rb') as fin, open(file_out,'wb') as fout:
    lines = fin.read().splitlines()
    case = 1
    a=1
    while a<len(lines):
        l=lines[a]
        ans=0
        n,p=map(int,l.split(' '))
        a+=1
        l=lines[a]
        if n==1:
            r=int(l)
            a+=1
            l=lines[a]
            q=map(int,l.split(' '))
            for j in range(0,p):
                x=float(q[j])/r
                y=round(x)
                if x>=0.9*y and x<=1.1*y:
                    ans+=1
        else:
            r1,r2=map(int,l.split(' '))
            a+=1
            l=lines[a]
            q1=map(int,l.split(' '))
            q1=sorted(q1)
            a+=1
            l=lines[a]
            q2=map(int,l.split(' '))
            q2=sorted(q2)
            list1=[]
            list2=[]
            for i in range(0,p):
                l=[]
                for k in range(int(math.ceil(q1[i]*10.0/(11*r1))),int(q1[i]*10.0/(9*r1)+1)):
                    l.append(k)
                list1.append(set(l))
                l=[]
                for k in range(int(math.ceil(q2[i]*10.0/(11*r2))),int(q2[i]*10.0/(9*r2)+1)):
                    l.append(k)
                list2.append(set(l))
            ilist=[]
            jlist=[]
            for i in range(0,p):
                for j in range(0,p):
                    if list1[i].intersection(list2[j])!=set():
                        if i not in ilist:
                            if j not in jlist:
                                ans+=1
                                ilist.append(i)
                                jlist.append(j)
        output = 'Case #%d: %s\n' % (case,ans)
	fout.write(output)
	case += 1
        a+=1

            