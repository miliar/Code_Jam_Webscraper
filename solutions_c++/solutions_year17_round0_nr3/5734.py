#include<iostream>
#include<fstream>
using namespace std;
int main(){

    ifstream inp;
    inp.open("C-small-1-attempt0.in");
    ofstream outf("Coutput.txt");
    unsigned long long t;

    inp>>t;
    for(unsigned long long i = 0; i < t; ++i){
        long long emptyBath, members, temp, count, baths, prevFound, found, prevCount, lastPos, countLeft, countRight;
        inp>>emptyBath>>members;
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
            found = 0;
            for(unsigned long long k = 0; k < baths; ++k){
                if(arr[k] == '.'){
                    ++count;
                }
                else if(arr[k] == 'O'){
                    if(count > prevCount){
                        prevCount = count;
                        prevFound = found;
                    }
                    found = k;
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
        cout<<countRight<<" "<<countLeft<<endl;
        outf << "Case #"<<i+1<<": "<<countRight<<" "<<countLeft<<endl;
        delete[] arr;
    }
    outf.close();
    inp.close();
}
