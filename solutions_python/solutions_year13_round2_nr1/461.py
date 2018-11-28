



FILE_PATH = "A-large.in"
PATH_OUTPUT = "out.txt"


def parseFile():

    f = open( FILE_PATH, "r" )

    first = True
    mode = 1
    lis = []
    lis2 = []
    for line in f.readlines():
        line = line.rstrip("\n")
        if not line:
            continue

        if first:
            first = False
            continue

        if mode == 1:
            lis2 = []
            for char in line.split(" "):
                lis2.append( int(char) )
            mode = 0
        else:
            mode = 1
            for char in line.split(" "):
                lis2.append( int(char) )
            lis.append(lis2)





    f.close()
    return lis

def main():
    x = parseFile()
    
    iteration = 1
    f = open( PATH_OUTPUT, "w")
    for lis in x:

         # Debug
        # iteration += 1
        # if iteration != 98:
        #     continue


        moteSize = lis[0]
        n = lis[1]
        motesList = lis[2:]

        winConList = []
        winCondition = 0
        winCondition2 = 0
        winCondition3 = 0

        # print moteSize
        # print motesList

        # Absorb
        failedToAbsorb = False
        while ( not failedToAbsorb ):
            failedToAbsorb = True
            for i in range( len(motesList) - 1, -1, -1):
                if motesList[i] < moteSize:
                    sizeRemoved = motesList.pop(i)
                    moteSize += sizeRemoved
                    failedToAbsorb = False

        # print moteSize
        # print motesList

        size = moteSize
        motesList.sort()

        winCondition2 = len(motesList)

        copied = list(motesList)
       
        while len(motesList) > 0:
            
            initialSize = moteSize
            moteSize += moteSize - 1 

            failedToAbsorb = False
            nAbsorbed = 0
            while ( not failedToAbsorb ):
                failedToAbsorb = True
                for i in range( len(motesList) - 1, -1, -1):
                    if motesList[i] < moteSize:
                        sizeRemoved = motesList.pop(i)
                        moteSize += sizeRemoved
                        nAbsorbed += 1
                        failedToAbsorb = False
            # print nAbsorbed
            if nAbsorbed > 0:
                winCondition += 1
            else:
                winCondition += 1
                motesList.pop()
                moteSize = initialSize
            winConList.append( winCondition + len(motesList))
        winConList.append(winCondition)
        winConList.append(winCondition2)

        moteSize = size
        if moteSize > 1:
            while len(copied) > 0:
                # print "copied", copied
                winCondition3 += 1
                moteSize += moteSize - 1 
                failedToAbsorb = False
                while ( not failedToAbsorb ):
                    failedToAbsorb = True
                    for i in range( len(copied) - 1, -1, -1):
                        if copied[i] < moteSize:
                            # print copied[i], moteSize
                            sizeRemoved = copied.pop(i)
                            moteSize += sizeRemoved
                            failedToAbsorb = False
                # winConList.append( winCondition3 )
                # print "append 3 if", winCondition3 + len(copied)
                winConList.append(winCondition3 + len(copied))
            winConList.append( winCondition3 )


        # print " win con list", winConList
        winCondition = min( winConList )


        # print winCondition
        # print "-------"
        if ( iteration == len(x) ):
            string = "Case #" + str(iteration) + ": " + str(winCondition)
        else:
            string = "Case #" + str(iteration) + ": " + str(winCondition) + "\n"
        f.write(string)
        iteration += 1

    f.close()






if __name__ == "__main__":
    main()