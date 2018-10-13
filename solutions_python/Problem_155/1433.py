def main():
    t=int(input())
    m=0
    while m<t:
        m+=1
        b=input().split()
        c=int(b[0])
        d=b[1]
        count=0
        sum=0
        for i in range(c+1):
            if(sum<i):
                count+=i-sum
                sum+=i-sum
            sum+=int(d[i])
        print("Case #%s: %s"%(m,count))

if (__name__ == "__main__"):
          main()
