__author__ = 'Mohit'

filename = "C://Temp/A-small-attempt0.in"
ins = open(filename, "r")
array = []
answers = []
for line in ins:
    array.append(line)

cases = array[0]
i = 1
j=1
while i < len(array):
    first_row = array[i]
    set1 = []
    line1 = array[i + int(first_row)]
    eles = line1.split(" ")
    for ele in eles:
        set1.append(int(ele))
    s1 = set(set1)
    second_row = array[i + 5]
    set2 = []
    line2 = array[i+5 + int(second_row)]
    eles = line2.split(" ")
    for ele in eles:
        set2.append(int(ele))
    s2 = set(set2)
    s3 = s1 & s2
    if len(s3) == 1:
        print "Case #"+str(j)+": "+str(list(s3)[0])
    elif len(s3) == 0:
        print "Case #"+str(j)+": Volunteer cheated!"
    else:
        print "Case #"+str(j)+": Bad magician!"
    i = i + 10
    j=j+1

ins.close()

