
n =int(raw_input())
k=1
for k in range(1,n+1):

 num=int(raw_input())

 for i in range(num,0,-1):
    num_str=str(i)
    l_list=list(num_str)
    if(all(l_list[i] <= l_list[i+1] for i in xrange(len(l_list)-1))):
        print("Case #%d: %r"%(k,i))
        break
    else:
        i=i-1
k=k+1