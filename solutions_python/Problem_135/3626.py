def magician(filename):
    f=open(filename,"r")
    aline=f.readline()
    aline = aline[:len(aline)-1]
    caseNumbers=int(aline)
    lines=f.readlines()
    f.close()

    for i in range(0,len(lines)):
        if i%5==0 and (i+5)%10!=0:
            case=(i+10)//10
            counter = 0
            guess1=[]
            guess2=[]
            aRow=lines[i]
            aRow=aRow[:len(aRow)-1]
            rowNumber=int(aRow)
            aline=lines[i+rowNumber]
            numbers1=aline.split(" ")
            for s in range(len(numbers1)):
                item = int(numbers1[s])
                guess1.append(item)
            bnumber=lines[i+5]
            bnumber=bnumber[:len(bnumber)-1]
            bnumber2=int(bnumber)
            bRow=lines[i+5+bnumber2]
            bRow=bRow[:len(bRow)-1]
            numbers2=bRow.split(" ")
            for i in range(len(numbers2)):
                item = int(numbers2[i])
                guess2.append(item)

            for x in guess1:
                for y in guess2:
                    if x==y:
                       number=x
                       counter=counter+1
            if   counter == 1:
                 print("Case #{}: {}".format(case,number))
            elif counter > 1 :
                 print("Case #{}: Bad magician!".format(case))
            elif counter == 0:
                 print("Case #{}: Volunteer cheated!".format(case))




