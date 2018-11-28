#include<iostream>
#include<fstream>
using namespace std;
int main(){


ifstream fi;
fi.open("C-small-1-attempt1.in"); //input file


ofstream fo;
fo.open("X.txt");



long testCases=0;

    fi>>testCases;

    for(unsigned long long i = 0; i < testCases; ++i){
        long long emptyBath, members, temp, count, baths, prevFound, mill, prevCount, lastPos, countLeft, countRight;

        fi>>emptyBath>>members;

        char *arr = new char[emptyBath + 2];
        arr[0] = 'O';
        arr[emptyBath + 1] = 'O';
        baths = emptyBath + 2;

        for(unsigned long long j = 1; j < emptyBath + 1; ++j){
            arr[j] = '.';
        }

        for(unsigned long long j = 0; j < members; ++j){
            count = 0;
            prevCount = -1;
            prevFound = 0;
            mill = 0;
            for(unsigned long long k = 0; k < baths; ++k){
                if(arr[k] == '.'){
                    ++count;
                }
                else if(arr[k] == 'O'){
                    if(count > prevCount){
                        prevCount = count;
                        prevFound = mill;
                    }
                    mill = k;
                    count = 0;
                }
            }
            arr[((prevCount + 1) / 2) + prevFound] = 'O';
        }

        lastPos = ((prevCount + 1) / 2) + prevFound;
        countLeft = 0;
        for(long long k = lastPos - 1; k >= 0 && arr[k] != 'O'; --k){
            ++countLeft;
        }
        countRight = 0;
        for(long long k = lastPos + 1; k < baths && arr[k] != 'O'; ++k){
            ++countRight;
        }
        fo<<"Case #"<<i+1<<": "<<countRight<<" "<<countLeft<<endl;
//        cout<<countRight<<" "<<cout<<endl;
        delete[] arr;
    }
fi.close();
fo.close();
}
