file1 = open("A-small-attempt0.in","r").read().split()
file2 = open("output","w")
T = int(file1[0])
i = 1
j = 1
results = []
form1, form2 = [[],[],[],[]], [[],[],[],[]]
while i <= T:
    row1 = int(file1[j])
    form1[0] = list(file1[j+1:j+5])
    form1[1] = list(file1[j+5:j+9])
    form1[2] = list(file1[j+9:j+13])
    form1[3] = list(file1[j+13:j+17])
    row2 = int(file1[j+17])
    form2[0] = list(file1[j+18:j+22])
    form2[1] = list(file1[j+22:j+26])
    form2[2] = list(file1[j+26:j+30])
    form2[3] = list(file1[j+30:j+34])
    for elem in form2[row2-1]:
        if elem in form1[row1-1]:
            results.append(elem)
    if len(results) == 0:
        file2.write("Case #"+str(i)+": Volunteer cheated!\n")
    elif len(results) == 1:
        file2.write("Case #"+str(i)+": "+str(results[0])+"\n")
    else:
        file2.write("Case #"+str(i)+": Bad magician!\n")
    results = []
    j += 34
    i += 1
    
    
    
    
