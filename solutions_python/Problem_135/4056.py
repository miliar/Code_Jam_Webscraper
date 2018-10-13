
lineList = open("file.txt").readlines()
outfile = open("outfile.txt","w")
case = 1
case_line = 1
LINES_PER_CASE = 10
for i in range(int(lineList[0])):#T test cases
    ans1 = int(lineList[case_line])
    ans2 = int(lineList[case_line+LINES_PER_CASE/2])
    list1 = [int(x) for x in lineList[case_line+ans1].split()]
    list2 = [int(x) for x in lineList[case_line+LINES_PER_CASE/2+ans2].split()]
    common_elements = []
    for j in list1:#find the common elements
        if j in list2:
            common_elements.append(j)
    if len(common_elements) == 1:
        outfile.write("Case #%d: %d\n"%(case,common_elements[0]))
    elif len(common_elements) == 0:
        outfile.write("Case #%d: Volunteer cheated!\n"%case)
    elif len(common_elements) > 1:
        outfile.write("Case #%d: Bad magician!\n"%case)
    case_line += LINES_PER_CASE
    case += 1

outfile.close()

print "done"  
  

