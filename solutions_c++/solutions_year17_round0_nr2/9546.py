#include<bits/stdc++.h>
#include <fstream>
#include <iostream>
using namespace std;

#define ll long long int

void shubh(){
  string s="love coding";
}

int main(){

    ofstream outfile;
    outfile.open("output.txt");

    ll T;
    string N;
    cin >> T;
    for(ll j=1;j<=T;j++){
        cin >> N;
        //counti=0;

        int siz=N.size();

        if(siz==1)
            {
                outfile << "Case #" << j << ": " << N << endl ;
                continue;
            }
        else{
        for(ll i=siz-1;i>0;i--){
            if((N[i]-'0')<(N[i-1]-'0')){
                if(N[i-1]=='0')
                    {
                     N[i-1]=N[i]='9';
                    }
                else
                {
                    N[i-1]=N[i-1]-1;
                    for(ll k=i;k<siz;k++)
                    N[k]='9';
                }
        }
      }
     }

    if(N[0]=='0')
        N.erase(0,1);
    outfile << "Case #" << j << ": " << N << endl ;

    }

    return 0;

    }
