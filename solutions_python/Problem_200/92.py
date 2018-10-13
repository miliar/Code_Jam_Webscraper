tidyinput = 'B-large.in'
tidyoutput = 'B-large.out'

inputlines = []
with open(tidyinput, 'r') as f:
    inputlines = f.readlines()

numcases = int(inputlines.pop(0))

def checktidy(number):
    numberstr = str(number)
    for i in range(len(numberstr)-1):
        if int(numberstr[i]) > int(numberstr[i+1]):
            return False
    return True

with open(tidyoutput,'w') as f:
    for x in range(numcases):
        number = inputlines.pop(0).strip()
        last = 0
        count = 0
        while not checktidy(number):
            count += 1
            last -= 1
            number = str(int(number[:last])-1)+count*'9'
        strtowrite = 'Case #'+str(x+1)+": "+str(int(number))+"\n"
        f.write(strtowrite)
