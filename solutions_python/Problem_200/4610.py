def is_tidy(number):
    string = str(number)
    for i in range(len(string)):
        if i == 0:
            #SKIP
            x = 1
        else:
            if int(string[i]) < int(string[i-1]):
                return False
    return True

def last_tidy(number):
    tidy_number = int(number)
    while not is_tidy(tidy_number):
        tidy_number -= 1
    return tidy_number


infile = open("INPUT.in")
outfile = open("OUTPUT.txt","w")

Skip = True
InputList = []
for line in infile:
    if Skip:
        Skip = False
    else:
        InputList.append(line.strip())

OutputList = []
for number in InputList:
    OutputList.append(last_tidy(number))

for i in range(len(OutputList)):
    outfile.write("Case #"+str(i+1)+": "+str(OutputList[i])+"\n")

outfile.close()
infile.close()
