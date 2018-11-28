# Written by Swapnik Shah
# swapnik.z@gmail.com


def process_case(sel_row1, sel_row2):
    i=0
    intersect = None
    while i<4:
        j=0
        while j<4:
            if sel_row1[i]==sel_row2[j]:
                if intersect != None:
                    return "Bad magician!"
                intersect = sel_row1[i]
            j+=1
        i+=1
    if intersect == None:
        return "Volunteer cheated!"
    else:
        return intersect


inF=open("A-small-attempt0.in",'r')

output = []

cases = 0

i = 0
sel_row1 = []
sel_row2 = []

row1 = row2 = 0

cr_case = 0
for each_line in inF:
    each_line = each_line.strip("\n")
    if i==0:
        cases = int(each_line)
        i+=1
        continue
    elif (i-1)%10 == 0:
        # new case
        if(cr_case!=0):
            # Process the case and return the answer
            output.append(process_case(sel_row1, sel_row2))
        cr_case +=1
        sel_row1 = []
        sel_row2 = []
        row1 = row2 = 0
        row1 = int(each_line)
        i+=1
    elif (i-1)%10 == 5:
        row2 = int(each_line)
        i+=1
    elif (i-1)%10 == row1:
        sel_row1 = each_line.split()
        i+=1
    elif (i-1)%10 == (row2+5):
        sel_row2 = each_line.split()
        i+=1
    else:
        i+=1
# Process last case
output.append(process_case(sel_row1, sel_row2))

inF.close()

outF = open("output.txt",'w')
i = 0
while i<cases:
    outF.write("Case #"+str(i+1)+": "+output[i]+"\n")
    i+=1
outF.close()
