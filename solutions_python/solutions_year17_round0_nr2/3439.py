a = int(input())
for value in range(1,a+1):
    b = input()
    for value2 in range(len(b)-1,0,-1):
        if int(b[value2]) < int(b[value2 -1]):
            c = str(int(b[value2-1]) -1)
            d = (len(b)-value2 )* "9"
            b = b[:value2 -1] + c + d
    print("Case #"+ str(value) + ":",int(b))
            

