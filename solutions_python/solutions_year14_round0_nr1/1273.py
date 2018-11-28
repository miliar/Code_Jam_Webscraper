

T=int(input())
for i in range(T):
    a=input()
    inp=[]
    for j in range(4):
        inp.append(input())
    data1 = set(map(int, inp[int(a)-1].split()))
    
    a=input()
    inp=[]
    for j in range(4):
        inp.append(input())        

    data2 = set(map(int, inp[int(a)-1].split()))

    o = len(data1.intersection(data2))

    if o == 0 :
        key = "Volunteer cheated!"
    elif o == 1 :
        key = str(data1.intersection(data2).pop())
    else :
        key = "Bad magician!"

    print ("Case #" + str(i+1) + ": " + key)
    
    
    
