file = open("B-small-attempt3.in", "r")
f = open('B-large.out', 'w')

testcases = int(file.readline())

print(testcases)

min = 0
max = 0

def by3(s):
    out = []
    while len(s):
        out.insert(0, s[-3:])
        s = s[:-3]
    return out
    
def by2(s):
    out = []
    while len(s):
        out.insert(0, s[-2:])
        s = s[:-2]
    return out

for i in range(0, testcases):
    number = int(file.readline())
    length = len(str(number));
      
    if(length == 1):
        f.write("Case #"+ str(i+1)+ ": "+ str(number) +"\n")
        print("Case #" + str(i + 1) + ": " + str(number) + "\n")
    elif(length == 2 or length == 3 or length == 4):
        for n in range(number, 0, -1):
            s = str(n)
            newS = ""
            list = ["2", "3", "4", "5", "6", "7", "8", "9"]
            st = [e for e in list if e in s]
            check = True
            if len(st) > 0:
                check = False

            if check == True:
                if(s[len(s)-1]== "0"):
                    numberOfOnes = len(s) - 1

                    for k in range(0, numberOfOnes):
                        newS = newS + "9"

                    s = newS
                    print("HERE ", s)
                    f.write("Case #"+ str(i+1)+ ": "+ s +"\n")
                    print("Case #" + str(i + 1) + ": " + s + "\n")
                    break

            sortedS = ''.join(sorted(s))

            if(s == sortedS):
                f.write("Case #"+ str(i+1)+ ": "+ s +"\n")
                print("Case #" + str(i + 1) + ": " + s + "\n")
                break
    else:
        if(length % 3 == 0):
            lst = by3(str(number))
        elif(length % 2 == 0):
            lst = by2(str(number))
        elif(length % 3 == 2):
            nnnn = str(number)
            lst = by3(nnnn[0:len(nnnn)-2])
            lst.append(nnnn[len(nnnn)-2: len(nnnn)])
        elif(length % 3 == 1):
            nnnn = str(number)
            lst = by2(nnnn[0:len(nnnn)-3])
            lst.append(nnnn[len(nnnn)-3: len(nnnn)])

        sortedList = []

        s = str(number)
        newS = ""
        list = ["2", "3", "4", "5", "6", "7", "8", "9"]
        st = [e for e in list if e in s]
        check = True
        if len(st) > 0:
            check = False

        if check == True:
            if(s[len(s)-1]== "0"):
                numberOfOnes = len(s) - 1

                for k in range(0, numberOfOnes):
                    newS = newS + "9"
                    
                s = newS
                f.write("Case #"+ str(i+1)+ ": "+ s +"\n")
                print("Case #" + str(i + 1) + ": " + s + "\n")
        else:
            for numm in lst:
                for n in range(int(numm), 0, -1):
                    s = str(n)
                   ## print(s)
                    newS = ""
                    list = ["2", "3", "4", "5", "6", "7", "8", "9"]
                    st = [e for e in list if e in s]
                    check = True
                    if len(st) > 0:
                      check = False

                    if check == True:
                      if(s[len(s)-1]== "0"):
                          numberOfOnes = len(s) - 1

                      for k in range(0, numberOfOnes):
                          newS = newS + "9"

                      s = newS

                sortedS = ''.join(sorted(s))

                if(s == sortedS):
                  sortedList.append(s)
                  break
        
            s = ''.join(sortedList)
            f.write("Case #"+ str(i+1)+ ": "+ s +"\n")
            print("Case #" + str(i + 1) + ": " + s + "\n")

f.close()
