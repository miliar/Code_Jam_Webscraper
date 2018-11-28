
#include<iostream>
#include<fstream>
#include<math.h>
#include<string>

using namespace std;
ifstream infile("A-large.in");
ofstream outfile("A_large_sol.in");

int main(){
    int times;
    long double dist,horses;

    long double pos,speed;
    int caser;
    caser=1;
    infile>>times;
    while(times--){
        infile>>dist;
        infile>>horses;
        long double time;
        int k=0;
        long double timer=0;
        for(k=0;k<horses;k++){
            infile>>pos;
            infile>>speed;
            time=(dist-pos)/speed;
            if(time>timer)
                timer=time;
        }
        outfile <<fixed;
        outfile<<"Case #"<<caser<<": "<<dist/timer<<endl;
        caser++;
    }


}
