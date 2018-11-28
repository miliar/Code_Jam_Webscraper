#include<iostream>
#include<fstream>
#include<string>
#include <iomanip>
using namespace std;


int main(){

    ofstream fo;
    fo.open("cruiseOutput1.txt");

    ifstream fi;
    fi.open("Ainp-large.in");

    int t;

    fi>>t;
    for(int ss = 0; ss < t; ++ss){
        double D;
        int N;
        double slowestHorse=0;
        double slowestTime=0;
        fi >> D >> N;
        double *K=new double[N];
        double *S=new double[N];
            for(int i=0;i<N;i++){
                fi >> K[i]>> S[i];
            }
            for(int i=0;i<N;i++){
                double horseTime=(D-K[i])/S[i];
                cout<< horseTime<<endl;
                if(horseTime > slowestTime){
                    slowestTime=horseTime;
                }

            }
               // std::cout << std::fixed << std::setprecision(6) << (float)D/slowestTime << std::endl;

            fo << std::fixed <<"Case #"<<ss+1<<": "<<std::setprecision(6)<<(float)D/slowestTime<<endl;

    }
}

