#include <iostream>
#include <string>
#include "string.h"
#include <fstream>
using namespace std;

bool checkIfRepeated(string gInput,int list_maxSize,int & gCurrentPutInList,string * checkList){

    if (gCurrentPutInList >= list_maxSize)
    {
        gCurrentPutInList = 0;
    }
    for (int i = 0; i < list_maxSize ; ++i) {
        if (gInput==checkList[i])
        {
            return true;
        }
    }
    return false;
}

int main() {

    int totalStrings=0;
    bool isfirstPut=true;
    ofstream outoutStream;
    outoutStream.open("/Users/shoaibanwar/ClionProjects/codeJamQ1/outputFile.txt");

    ifstream inputStream;
    inputStream.open("/Users/shoaibanwar/ClionProjects/codeJamQ1/A-large.in");
    if (inputStream.is_open())
    {
        inputStream>>totalStrings;
    }

    string input0;
    int k0;
    int cCase=1;
    for (int m = 0; m < totalStrings ; ++m) {
        inputStream.ignore();
        getline(inputStream,input0,' ');
        inputStream>>k0;

        int len = input0.length();
        int countApplied=0;
        int currentPutInList=0;
        string *checkList = new string[2*k0];

        bool toWriteCount=true;

        for (int l = 0; l < 2*k0 ; ++l) {
            checkList[l] = "default";
        }

       // int negIndex_when_k_outofBound = -1;
        int i=0;
        for (i = 0; i < len; ++i)
        {

            if (input0[i]=='-')
            {
                if (i+k0-1 < len)
                {
                    int firstNegIndex= -1;
                    countApplied++;
                    input0[i] = '+';
                    int j=1;
                    for (j = 1; j < k0 ; ++j) {
                        if (input0[i+j]=='+')
                        {
                            input0[i+j] = '-';
                            //if (firstNegIndex==-1)
                            //{
                            //    firstNegIndex= i+j;
                            //}
                        }
                        else
                        {
                            input0[i+j] = '+';
                        }
                    }
                    //negIndex_when_k_outofBound = firstNegIndex;
                }
                else
                {
                    //if (negIndex_when_k_outofBound!= -1)
                    //{
                    //    i= negIndex_when_k_outofBound;
                    //}
                    //else{
                    //    toWriteCount=false;
                    //}
                    if (isfirstPut==false)
                    {
                        outoutStream<<endl;
                    }
                    outoutStream<<"Case #"<<cCase<<": "<<"IMPOSSIBLE";
                    cCase++;
                    toWriteCount=false;
                    isfirstPut=false;
                    break;
                }
                bool Rep=checkIfRepeated(input0,2*k0,currentPutInList,checkList);
                if (Rep)
                {
                    if (isfirstPut==false)
                    {
                        outoutStream<<endl;
                    }
                    outoutStream<<"Case #"<<cCase<<": "<<"IMPOSSIBLE";
                    cCase++;
                    toWriteCount=false;
                    isfirstPut=false;
                    break;
                }
                cout<<endl<<input0<<endl;
                checkList[currentPutInList]=input0;
                currentPutInList++;
            }

        }
        if (toWriteCount)
        {
            if (isfirstPut==false)
            {
                outoutStream<<endl;
            }
            outoutStream<<"Case #"<<cCase<<": "<<countApplied;
            cCase++;
            isfirstPut=false;
        }
    }
    outoutStream.close();
    return 0;
}