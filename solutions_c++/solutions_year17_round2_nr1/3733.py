#include<iostream>
#include<stdio.h>
#include<string>
#include <algorithm>
#include <iomanip>
using namespace std;

int main(){
    int ch,caseno;


    cin >> ch;
    for (caseno=1;caseno<=ch;caseno++){
        double dd,nn;
        double ddh[2000]={0},kkh[2000]={0};
        double tth[2000]={0},maxt=0.0,res;
        cin >> dd >> nn;
        for (int in=1;in<=nn;in++){
            cin >> ddh[in] >> kkh[in];
            tth[in]= ((dd - ddh[in])/kkh[in]);
            //cout << tth[in];
            if(in==1){maxt = tth[in];}
            if(in>1){
                if(tth[in]>maxt){
                    maxt=tth[in];
                }
            }
        }
        res=dd/maxt;

        //cout << "Case #" << caseno << ": " << std::setprecision(7) << res << endl;
        cout << "Case #" << caseno << ": ";

        printf("%.6f",res);cout <<endl;


    }
    return 0;
}
