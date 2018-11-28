#include <iostream>
#include <string>
#include <math.h>
#include <fstream>

using namespace std;

int* leftRightDist(int* stalls, int stallNumber){
    int* answer = new int[2];
    int stallNumberTemp = stallNumber - 1;

    //Calculate ls
    for(stallNumberTemp; stalls[stallNumberTemp] == 0; stallNumberTemp--){}
    answer[0] = stallNumber - stallNumberTemp - 1;

    //Calculate rs
    stallNumberTemp = stallNumber + 1;
    for(stallNumberTemp; stalls[stallNumberTemp] == 0; stallNumberTemp++){}
    answer[1] = stallNumberTemp - stallNumber - 1;
    return answer;
}

int main()
{
    ifstream inputFile("input.txt");
    ofstream outFile("output.txt");
    int numStalls;
    int numPeople;
    int numberOfCases;
    inputFile>>numberOfCases;

    for(int c = 0; c < numberOfCases; c++){
        inputFile>>numStalls>>numPeople;
        //Initialise the stalls array
        int* stalls = new int[numStalls + 2];
        for(int i = 0; i < numStalls + 2; i++){
            stalls[i] = 0;
        }
        stalls[0] = 1;
        stalls[numStalls + 1] = 1;

        int minLs;
        int minRs;
        int bestStallPosition = 0;
        int* lsrs;
        for(int n = 0; n < numPeople; n++){
            bestStallPosition = 0;
            minLs = -1;
            minRs = -1;
            for(int i = 1; i < numStalls + 1; i++){
                if(stalls[i] == 0){
                    lsrs = leftRightDist(stalls, i);
                    if(min(lsrs[0], lsrs[1]) > min(minLs, minRs)){
                        minLs = lsrs[0];
                        minRs = lsrs[1];
                        bestStallPosition = i;
                    }else if(min(lsrs[0], lsrs[1]) == min(minLs, minRs)){
                        if(max(lsrs[0], lsrs[1]) > max(minLs, minRs)){
                            minLs = lsrs[0];
                            minRs = lsrs[1];
                            bestStallPosition = i;
                        }
                    }
                }
            }
            stalls[bestStallPosition] = 1; //This person takes up this stall
        }
        outFile<<"Case #"<<c + 1<<": "<<max(minLs, minRs)<<" "<<min(minLs, minRs)<<endl;
        delete[] stalls;
    }
    return 0;
}
