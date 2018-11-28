#include<iostream>
#include<stdio.h>
using namespace std;
int main (){
    int t;
    double d, n, k, s, k1, s1, k2, s2, time1, time2, time, distance, velocity;
    cin>>t;
    for(int ii = 1; ii <= t; ii++){
        cout<<"Case #"<<ii<<": ";
        cin>>d>>n;
        if(n == 1){
            cin>>k>>s;
            distance = (d - k);
            time = distance / s;
            velocity = d / time;
        }
        else{
            cin>>k1>>s1>>k2>>s2;
            time1 = (d - k1) / s1;
            time2 = (d - k2) / s2;
            time = max(time1, time2);
            velocity = d / time;
        }
        printf("%0.6f \n", velocity);
    }
}
