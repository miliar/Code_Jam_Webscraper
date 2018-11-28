#include<iostream>
#include<fstream>
int main(){

    std::ifstream iF("C-small-1-attempt0.in");
    std::ofstream oF("output.txt");
    unsigned long long t;
    iF>>t;
    for(unsigned long long i = 0; i < t; i++){
        long long e, m, c, baths, prevFound, found, prevCount, lastPos, countLeft, countRight;
        iF>>e>>m;
        char *arr = new char[e + 2];
        arr[0] = 'O';
        arr[e + 1] = 'O';
        baths = e+2;
        for(unsigned long long j = 1; j < e + 1; ++j){
            arr[j] = '.';
        }
        for(unsigned long long j = 0; j < m; ++j){
            c = 0;
            prevCount = -1;
            prevFound = 0;
            found = 0;
            for(unsigned long long k = 0; k<baths; k++){
                if(arr[k] == '.'){
                    c++;
                }
                else if(arr[k] == 'O'){
                    if(c>prevCount){
                        prevCount = c;
                        prevFound = found;
                    }
                    found=k;
                    c=0;
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
        oF<<"Case #"<<i+1<<": "<<countRight<<" "<<countLeft<<std::endl;
        delete[] arr;
    }
    oF.close();
    iF.close();
}
