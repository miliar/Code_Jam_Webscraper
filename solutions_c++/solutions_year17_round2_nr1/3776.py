#include<iostream>
#include<bits/stdc++.h>
using namespace std;

#define ll long long

vector< pair<ll,ll> > vec;



ifstream inf("input.txt");
ofstream ouf("output.txt");



int main(){
    int T;
    ll K,D,N,S;
    FILE * fp;

   fp = fopen ("output.txt", "w+");
    double minitme=-1.0d;
    inf >> T;
    for(int i=1;i<=T;i++){
            minitme=-1.0d;
       inf >> D >> N ;
       for(int j=0;j<N;j++){
        inf >> K >> S ;
        vec.push_back({K,S});
        double tmp=float(D-K)/S;
       // cout << tmp;
        if(tmp>minitme)
            minitme=tmp;
        }

        fprintf(fp,"Case #%d: %0.6f\n",i,(double(D)/minitme));

        vec.clear();
    }

    return 0;

    }
