#include<stdio.h>
#include<stdlib.h>
#include<fstream>
#include<iostream>

using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    in.open("inputLarge.txt");
    out.open("outputLarge.txt");
    int t,cases=0;
    in>>t;
    while(t--)
    {
        cases++;
        long long int D,N;
        in>>D>>N;
        long long int start;
        int speed;
        double time;
        double maxTime = 0;
        for(int i=0;i<N;i++)
        {
            in>>start>>speed;
            time = ((D-start)*1.0)/speed;
            if(time>maxTime) maxTime = time;
        }
        double maxSpeed=0;
        maxSpeed = D/maxTime;
        out<<"Case #"<<cases<<": "<<fixed<<maxSpeed<<endl;
    }
    return 0;
}
