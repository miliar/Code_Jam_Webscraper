
import sys

def main():
    pass

if __name__ == '__main__':
    main()

Inputfile = open("%s" % sys.argv[1], 'r')
Outputfile = open("%s.out" % sys.argv[1][:-3], 'w')

testCasesCount = Inputfile.readline()

for i in range (0,int(testCasesCount)):
    newLine =  Inputfile.readline()

    maxShynessLevel = newLine[0]
    SumOfPeople = 0
    FriendsAdded = 0
    #print "\n\nNew Test Set \n\n"
    for j in range (0,int(maxShynessLevel)+1):

        print "J = "+ str(j) + "\nNewLine2+j = " + newLine[2+j] + "\n SumThusFar = " + str(SumOfPeople)
        if(int(newLine[2+j]) > 0):

            if (SumOfPeople+FriendsAdded < j):

                FriendsAdded = FriendsAdded + (j - (SumOfPeople+FriendsAdded))

            print "Friends Added " + str(FriendsAdded)


        SumOfPeople = int(SumOfPeople) + int(newLine[2+j])

    print "Friends Added " + str(FriendsAdded) + " : "+newLine

    #print "Case #"+str(i+1)+": "+str(FriendsAdded)
    Outputfile.write("Case #"+str(i+1)+": "+str(FriendsAdded)+"\n")

Outputfile.close()
Inputfile.close()