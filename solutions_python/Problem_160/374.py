#coding:utf-8

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd (a, b)

def lcm_list(a):
    tmp=a[0]
    for i in a:
        tmp=lcm(tmp,i)
    return tmp

def main():
    fr=open("B-small-attempt5.in","r")
    output=""
    ans=[]
    casenum=0
    count=0
    B=0
    N=0
    for line in fr:
        #print(count)
        if count==0:
            casenum=int(line)
        else:
            tmpans=0
            if (count%2) == 1:
                B,N = map(int, line.split())
            else:
                if N <= B:
                    print(int(N))
                    ans.append(int(N))
                else:
                    originalvals=[int(cell) for cell in line.split()]
                    time=lcm_list(originalvals)#周期
                    print(time,end=":")
                    tmp=sum([time/i for i in originalvals])
                    N=(N-1)%tmp+1
                    if N <= B:
                        print(int(N))
                        ans.append(int(N))
                    else:
                        vals=[int(cell) for cell in line.split()]
                        i=B
                        b=0
                        while i<N:
                            b=vals.index(min(vals))
                            vals[b]=vals[b]+originalvals[b]
                            i=i+1
                        print(b+1)
                        ans.append(b+1)
        count=count+1

    for i in range(0,casenum):
        output=output+"Case #"+str(i+1)+": "+str(ans[i]) + "\n"

    fr.close()


    fw=open("out.txt","w")
    fw.write(output)
    fw.close()

main()