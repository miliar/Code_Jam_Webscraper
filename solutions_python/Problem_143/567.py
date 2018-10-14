def main():
    f=open('/home/ayush/B-small-attempt0.in','r')
    o = open("/home/ayush/Downloads/output.txt",'w')
    t=int(f.readline())
    x=0
    while t:
        t-=1
        x+=1
        count=0
        a,b,k = map(int,f.readline().split())
        for i in range(1,a):
            for j in range(1,b):
                if i&j < k:
                    count+=1
        o.write('Case #%d: %d\n'%(x,count+a+b-1))
main()
        
