def magic(f="E:\\Users\\Neta\\Downloads\\A-small-attempt0.in"):
    file = open(f, 'r')
    iternumber=int(file.readline().replace("\n",""))
    for i in range(iternumber):
        p=[0,0,0,0]
        t=[0,0,0,0]
        num=file.readline().replace("\n","")
        counter=0
        magicnumber=0
        for j in range(int(num)):
            k=file.readline().replace("\n","")
            k=k.split(" ")
            p[0]=k[0]
            p[1]=k[1]
            p[2]=k[2]
            p[3]=k[3]
        for j in range(4-int(num)):
            file.readline().replace("\n","")
        num=file.readline().replace("\n","")
        for j in range(int(num)):
            k=file.readline().replace("\n","")
        k=k.split(" ")
        t[0]=k[0]
        t[1]=k[1]
        t[2]=k[2]
        t[3]=k[3]
        for j in range(4):
            if t[j] in p:
                counter=counter+1
                magicnumber=t[j]
        for j in range(4-int(num)):
            file.readline().replace("\n","")
        if counter==0:
            print("Case #"+str(i+1)+": Volunteer cheated!")
        if counter>1:
            print("Case #"+str(i+1)+": Bad magician!")
        if counter==1:
            print("Case #"+str(i+1)+": "+magicnumber)

