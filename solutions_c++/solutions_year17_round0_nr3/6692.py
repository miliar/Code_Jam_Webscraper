#include<iostream>
#include<fstream>
#define ull unsigned long long

using namespace std;
int main(){

    ifstream inputFile("C-small-1-attempt1.in");
    ofstream ouputFile("output.txt");
    ull t=0;

    inputFile>>t;
    for(ull i = 0; i < t; ++i){
        long long mems=0, copy=0, ctr=0, baths_time=0, prevFound=0, found=0, prevCount=0, lastPos=0, countLeft=0, countRight;
        long long free_bath=0;

        inputFile>>free_bath>>mems;
        char *array = new char[free_bath + 2];
        array[0] = 'O';
        array[free_bath + 1] = 'O';
        baths_time = free_bath + 2;

        for(unsigned long long j = 1; j < free_bath + 1; ++j){
            array[j] = '.';
        }

        for(unsigned long long j = 0; j < mems; ++j){
            ctr = 0;
            prevCount = -1;
            prevFound = 0;
            found = 0;
            for(unsigned long long k = 0; k < baths_time; ++k){
                if(array[k] == '.'){
                    ctr++;
                }
                else if(array[k] == 'O'){
                    if(ctr > prevCount){
                        prevCount = ctr;
                        prevFound = found;
                    }
                    found = k;
                    ctr = 0;
                }
            }
            array[((prevCount + 1) / 2) + prevFound] = 'O';
        }

        lastPos = ((prevCount + 1) / 2) + prevFound;
        countLeft = 0;
        for(long long k = lastPos - 1; k >= 0 && array[k] != 'O'; --k){
            countLeft++;
        }
        countRight = 0;
        for(long long k = lastPos + 1; k < baths_time && array[k] != 'O'; ++k){
            countRight++;
        }
        ouputFile<<"Case #"<<i+1 <<": " <<countRight<<" "<<countLeft<<"\n";
        delete[] array;
    }
    ouputFile.close();
    inputFile.close();
}
