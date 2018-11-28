#include<iostream>
#include<fstream>
using namespace std;


int main(){
    ifstream in;
    in.open("C-small-1-attempt1.in");

    ofstream out;
    out.open("Coutput.txt");

    unsigned long long t;

    in>>t;

    for(unsigned long long i = 0; i< t; ++i){
        long long last_position, eBathRoom, memory, temp;
        long long counters, foud, bathroom, prevFound;
        long long prevCount, leftCounters, rightCounters;
        in>>eBathRoom>>memory;
        char *arr = new char[eBathRoom + 2];
        arr[0] = 'O';

        bathroom = eBathRoom + 2;
        arr[eBathRoom + 1] = 'O';
        for(unsigned long long j = 1; j < eBathRoom + 1; j++)
        {
            arr[j] = '.';
        }
        for(unsigned long long j = 0; j < memory; j++)
        {
            prevFound = 0;
            foud = 0;
            counters = 0;
            prevCount = -1;

            for(unsigned long long k = 0; k < bathroom; k++)
            {
                if(arr[k] == '.')
                {
                    ++counters;
                }
                else if(arr[k] == 'O')
                {
                    if(counters > prevCount)
                    {
                        prevCount = counters;
                        prevFound = foud;
                    }
                    foud = k;
                    counters = 0;
                }
            }
            arr[ ((prevCount+1)/ 2)+prevFound]='O';
        }
        last_position = ((prevCount + 1) / 2) + prevFound;
        leftCounters = 0;

        for(long long k = last_position - 1; k >= 0 && arr[k] != 'O'; --k)
        {
            ++leftCounters;
        }
        rightCounters = 0;
        for(long long k = last_position + 1; k < bathroom && arr[k] != 'O'; ++k){
            ++rightCounters;
        }
        cout<<rightCounters<<" "<<leftCounters<<endl;
        out<< "Case #"<<i+1<<": "<<rightCounters<<" "<<leftCounters<<endl;
        delete[] arr;
    }
    out.close();
    in.close();
}
