T = int(input())

for c in range(1,T+1):
    num = input()
    nlist = list(num)
    nlist.sort()
    nums = ''.join(nlist)

    if nums == num:
        print("Case #"+str(c)+": "+num)
    else:
        while nums != num:
            num = str(int(num)-1)
            nlist = list(num)
            nlist.sort()
            nums = ''.join(nlist)
        print("Case #"+str(c)+": "+num)
    
    
