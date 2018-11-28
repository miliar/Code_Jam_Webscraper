
def lastTidyNumber(num):
    counter=1
    while(counter<=num):
        dig = list(int(d) for d in str(counter))
        # print(dig)
        dig1 = sorted(dig)
        # print(dig1)
        num1 = int(''.join(map(str, dig1)))
        # print(num1)
        if counter == num1:
            # print("Tidy Numbers")
            lastTidyNumber=counter
        # else:
        #     print("Not Tidy Numbers")
        counter+=1
    return(lastTidyNumber)
    # print("The Last Tidy Number: "+str(lastTidyNumber))
outputfile = open('B-small-attempt1-output1.txt','w')
with open('B-small-attempt1.in') as inputfile:
    lines = inputfile.read().splitlines()

n=int(lines[0])
for x in range(1,n+1):
    value=lastTidyNumber(int(lines[x]))
    outputfile.write("case #"+str(x)+": "+str(value)+"\n")
