for n in range(int(input())):
    num = input()
    for d in range(len(num)-2, -1, -1):
        if int(num[d]) > int(num[d+1]):
            num = num[:d] + str(int(num[d])-1) + "9" * (len(num)-d-1)
    while num[0] == "0":
        num = num[1:]
    print("Case #%d: %s"%(n+1, num))
