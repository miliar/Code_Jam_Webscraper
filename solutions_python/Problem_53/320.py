t=raw_input()
test=int(t)
for i in range(0,test):
    a=raw_input()
    (num,kay)=a.split(" ")
    n=int(num)
    k=int(kay)
    p=2**n
    if((k+1)%p==0):
        print "Case #" + str(i+1) + ": ON"
    else:
        print "Case #" + str(i+1) + ": OFF"
