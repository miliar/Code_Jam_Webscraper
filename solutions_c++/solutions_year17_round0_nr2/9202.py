//
// Created by tanishka on 8/4/17.
//
#include<bits/stdc++.h>
#define boost std::ios::sync_with_stdio(false);
#define cin std::cin
#define cout std::cout
#define MAX 1000056
using namespace std;
typedef long long  ll;
typedef unsigned long long ull;


int main(){
    boost;
    int t;
    cin>>t;
    ull n;
    int nos[20];
    int cp[20];
    for(int bj=1;bj<=t;bj++){
        cin>>n;
        int i;
        i=0;
        while(n>0){
            cp[i]=(n%10);
            n=n/10;
            i++;
        }
        for(int j=0;j<i;j++){
            nos[j]=cp[i-j-1];
        }
       int ind=0;
        bool flag=true;
        for(int j=0;j<i-1;j++){
           if(nos[j]>nos[j+1]){
               ind=j;
               flag=false;
               break;
           }

       }
        //nos[ind]=nos[ind]-1;
       //bool flag=true;
        if(!flag) {
            for (int j = ind; j > 0; j--) {
                if (nos[j] != nos[j - 1]) {
                    ind = j;

                    //flag=false;
                    break;
                } else {
                    if (j == i) {
                        break;
                    } else {
                        ind--;
                    }
                }
            }
        }
        //cout<<ind<<"\n";

        if(ind!=i-1&&!flag)
            nos[ind]=nos[ind]-1;

       if(!flag) {
           for (int j = ind + 1; j < i; j++) {
               nos[j] = 9;
           }
       }
       ull final =0;
       ull mul=1;
       for(int j=i-1;j>=0;j--){
           final =final+nos[j]*mul;
           mul=mul*10;
       }
       cout<<"Case #"<<bj<<":"<<" "<<final<<"\n";
    }
    return 0;
}
