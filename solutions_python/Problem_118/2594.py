def main():
    file=open("C-small-attempt2.in","r")
    out=open("google_it.txt","w")
    
    n=int(file.readline().strip())

 
    for case in range(1,n+1):
        count=0
        temp=file.readline().strip()
        temp=temp.split()
        a=int(temp[0])
        b=int(temp[1])

        for i in range(a,b+1):
            if i**0.5==round(i**0.5):
                i_rev=int(str(i)[::-1])
                small_i=round(i**0.5)
                small_i_rev=int(str(small_i)[::-1])
                if i_rev==i and small_i==small_i_rev:
                    count+=1
        out.write("Case #%d: %d\n" %(case,count))
    file.close()
    out.close()

main()

