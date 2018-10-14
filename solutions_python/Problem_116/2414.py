#!/usr/bin/python3

def ticTacToeTomek() :
    fread = open("A-large.in","r")
    fwrite = open("output.txt","w")
    x = int(fread.readline())
    for j in range(0,x):
        xflag = False
        oflag = False
        drawflag = False
        gameoverflag = True
        checkFlag = False
        diag1 = ""
        diag2 = ""
        col1 = ""
        col2 = ""
        col3 = ""
        col4 = ""

        for i in range(0,4):
            inputrow = fread.readline()
            if(gameoverflag == True):
                dotindex = inputrow.find(".")
                if(dotindex != -1):
                    gameoverflag = False
            inputval = inputrow[:4]
            if(inputval == "XXXT" or inputval == "XXTX" or inputval == "XTXX" or inputval == "TXXX" or inputval == "XXXX" ):
                xflag = True
                checkFlag = True
                break
            elif(inputval == "OOOT" or inputval == "OOTO" or inputval == "OTOO" or inputval == "TOOO" or inputval == "OOOO"):
                oflag = True
                checkFlag = True
                break
            else:
                diag1 += inputval[i]
                diag2 += inputval[3-i]
                col1 += inputval[0]
                col2 += inputval[1]
                col3 += inputval[2]
                col4 += inputval[3]

        if(checkFlag == False):
            if(diag1 == "XXXT" or diag1 == "XXTX" or diag1 == "XTXX" or diag1 == "TXXX" or diag1 == "XXXX" ):
                xflag = True

            elif(diag1 == "OOOT" or diag1 == "OOTO" or diag1 == "OTOO" or diag1 == "TOOO" or diag1 == "OOOO"):
                oflag = True
        
            elif(diag2 == "XXXT" or diag2 == "XXTX" or diag2 == "XTXX" or diag2 == "TXXX" or diag2 == "XXXX" ):
                xflag = True

            elif(diag2 == "OOOT" or diag2 == "OOTO" or diag2 == "OTOO" or diag2 == "TOOO" or diag2 == "OOOO"):
                oflag = True
           
            elif(col1 == "XXXT" or col1 == "XXTX" or col1 == "XTXX" or col1 == "TXXX" or col1 == "XXXX" ):
                xflag = True
    
            elif(col1 == "OOOT" or col1 == "OOTO" or col1 == "OTOO" or col1 == "TOOO" or col1 == "OOOO"):
                oflag = True
           
            elif(col2 == "XXXT" or col2 == "XXTX" or col2 == "XTXX" or col2 == "TXXX" or col2 == "XXXX" ):
                xflag = True

            elif(col2 == "OOOT" or col2 == "OOTO" or col2 == "OTOO" or col2 == "TOOO" or col2 == "OOOO"):
                oflag = True
           
            elif(col3 == "XXXT" or col3 == "XXTX" or col3 == "XTXX" or col3 == "TXXX" or col3 == "XXXX" ):
                xflag = True
          
            elif(col3 == "OOOT" or col3 == "OOTO" or col3 == "OTOO" or col3 == "TOOO" or col3 == "OOOO"):
                oflag = True
          
            elif(col4 == "XXXT" or col4 == "XXTX" or col4 == "XTXX" or col4 == "TXXX" or col4 == "XXXX" ):
                xflag = True

            elif(col4 == "OOOT" or col4 == "OOTO" or col4 == "OTOO" or col4 == "TOOO" or col4 == "OOOO"):
                oflag = True
        else:
            for k in range(i+1,4):
                fread.readline()

        if(xflag == True):
            fwrite.write("Case #%d: X won" %(j+1))
            fwrite.write("\n")
        
        elif(oflag == True):
            fwrite.write("Case #%d: O won" %(j+1))
            fwrite.write("\n")
        elif(gameoverflag == False):
            fwrite.write("Case #%d: Game has not completed" %(j+1))
            fwrite.write("\n")
        else :
            fwrite.write("Case #%d: Draw" %(j+1))
            fwrite.write("\n")
        fread.readline()

    fread.close()
    fwrite.close()

if __name__ == "__main__":
    ticTacToeTomek()
