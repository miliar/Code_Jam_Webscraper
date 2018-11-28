#include<iostream>
#include<fstream>
using namespace std;


int main(){

    ifstream in;
    in.open("C-small-1-attempt0.in");

    ofstream out;
    out.open("Coutput.txt");

    unsigned long long t;

    in>>t;

    for(unsigned long long i = 0; i< t; ++i){
        long long lastPosition, eBath, mem, temp;
        long long counter, foud, bath, previousFound;
        long long previousCount, counterLeft, counterRight;
        in>>eBath>>mem;
        char *arr = new char[eBath + 2];
        arr[0] = 'O';


        bath = eBath + 2;
    arr[eBath + 1] = 'O';
        for(unsigned long long j = 1; j < eBath + 1; ++j){

            arr[j] = '.';
        }

        for(unsigned long long j = 0; j < mem; ++j){

            previousFound = 0;
            foud = 0;

            counter = 0;
            previousCount = -1;

            for(unsigned long long k = 0; k < bath; ++k){

                if(arr[k] == '.'){

                    ++counter;
                }
                else if(arr[k] == 'O'){

                    if(counter > previousCount){

                        previousCount = counter;

                        previousFound = foud;
                    }

                    foud = k;

                    counter = 0;
                }
            }

                arr[ ((previousCount+1)/ 2)+previousFound]='O';
        }


            lastPosition = ((previousCount + 1) / 2) + previousFound;

        counterLeft = 0;

        for(long long k = lastPosition - 1; k >= 0 && arr[k] != 'O'; --k){

                ++counterLeft;

        }

        counterRight = 0;
        for(long long k = lastPosition + 1; k < bath && arr[k] != 'O'; ++k){

                ++counterRight;

        }


        cout<<counterRight<<" "<<counterLeft<<endl;
        out<< "Case #"<<i+1<<": "<<counterRight<<" "<<counterLeft<<endl;
        delete[] arr;
    }


    out.close();
    in.close();
}
