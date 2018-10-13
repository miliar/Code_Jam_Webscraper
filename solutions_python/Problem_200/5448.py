import numpy as np
import sys

def checkIfTidy(N):
    if(N<10):
        return True
    string_N = str(N)
    for i in range(len(string_N)-1):
        if(int(string_N[i]) > int(string_N[i+1])):
            return False
    return True

def getLastUntidyIndex(N):
    string_N = str(N)
    for i in reversed(range(len(string_N)-1)):
        if(int(string_N[i]) > int(string_N[i+1])):
            return i

def getLastTidyRecur(N):
    if(checkIfTidy(N)):
        return N
    else:
        untidyIndex = getLastUntidyIndex(N)
        string_N = str(N)
        list_N = list(string_N)
        
        untidyBig = int(list_N[untidyIndex])
        untidySmall = int(list_N[untidyIndex+1])
        list_N[untidyIndex] = str(untidyBig-1)
        
        
        for i in range(untidyIndex+1,len(list_N)):
            list_N[i] = str(9)
        
        string_N = ''.join(list_N)
        #print string_N
        return getLastTidyRecur(int(string_N))
        


if __name__ == "__main__":
    file_name = sys.argv[1]
    print file_name
    A_input = np.genfromtxt(file_name,dtype='i4')
    #print A_input
    # A_input = [3,132,1000,2]
    case_num = A_input[0]

    for idx in range(1,case_num+1):
        ans =  "Case #"+str(idx) + ": " +  str(getLastTidyRecur(A_input[idx]))
        #print A_input[idx]
        print ans
        with open('output','a') as outputFile:
            outputFile.write(ans + '\n')