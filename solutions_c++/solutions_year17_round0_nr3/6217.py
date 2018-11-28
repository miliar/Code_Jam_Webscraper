#include <iostream>
#include "TMath.h"
#include<fstream>
#include<vector>

#include<string>

using namespace std;
using namespace TMath;

long aMax=0;
long aMin=0;

void BathroomStalls(long N, long K);

int main() {

    ifstream inPutFile;
    ofstream outPutFile;

    inPutFile.open("/Users/zhuj/Downloads/C-small-2-attempt0.in");
    outPutFile.open("/Users/zhuj/Downloads/B-output.txt");

    if(!inPutFile){
        cout<<"can not find the doc"<<endl;
    }

    long t, n, m;

    inPutFile >> t;
    for (long i = 1; i <= t; ++i) {
        inPutFile >> n >> m;
        aMax = 0;
        aMin = 0;
        BathroomStalls(n, m);
        outPutFile << "Case #" << i << ": " << aMax << " " << aMin << endl;
    }

    inPutFile.close();
    outPutFile.close();

//    cin >> t;
//    for (long i = 1; i <= t; ++i) {
//        cin >> n >> m;
//        aMax = 0;
//        aMin = 0;
//        BathroomStalls(n,m);
//        cout << "Case #" << i << ": " << aMax << " " << aMin << endl;
//    }

    return 0;
}

void BathroomStalls(long N, long K){
    long double averLR;
    long stall;
    long emptyBar;
    long ni;

    for(long n=1;n<30;n++){
        emptyBar=(long)powl(2,n);
        stall=(long)powl(2,n)-1;

        if(K>=(long)powl(2,n-1) && K<=stall){
            ni=n;
            break;
        }
    }
    averLR=(N-stall)/powl(2,ni); //to get a double

    //solve the equation
    // ceill*ac+floorl*af=stall
    // ac+af=emptyBar

    


    if(averLR-floorl(averLR)>=0.5){
        long acf=((long)ceill(averLR))*((long)powl(2,ni+1)-(long)powl(2,ni))+(long)powl(2,ni)-N-1; //the pair number (c,f)
        long acc=(long)powl(2,ni)-(long)powl(2,ni-1)-acf;                                                          //the (c,c)

        if(K>(long)powl(2,ni-1)-1+acc){            //count the (c,c) first
            aMax=(long)ceill(averLR);
            aMin=(long)floorl(averLR);
        }else{
            aMax=(long)ceill(averLR);
            aMin=aMax;
        }
    }else{
        long acf=(-1*(long)floorl(averLR))*((long)powl(2,ni+1)-(long)powl(2,ni))-(long)powl(2,ni)+N+1; //the pair number (c,f)
        long aff=(long)powl(2,ni)-(long)powl(2,ni-1)-acf;                                                        //the (c,c)

        if(K>(long)powl(2,ni-1)-1+acf){            //count the (c,f) first
            aMin=(long)floorl(averLR);
            aMax=aMin;
        } else{
            aMax=(long)ceill(averLR);
            aMin=(long)floorl(averLR);
        }
    }
}