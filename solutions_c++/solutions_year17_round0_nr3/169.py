#include <iostream>
#include <algorithm>
using namespace std;
int tc;
long long n,k;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>tc;
    for(int ct=1;ct<=tc;++ct){
        cin>>n>>k;
        int digitcount=CHAR_BIT*sizeof(long long)-__builtin_clzll(k);
        long long usedcount=(1ll<<(digitcount-1));
        n-=(usedcount-1ll);
        long long offset=k-usedcount;
        long long width=(n+usedcount-1-offset)/usedcount;
        long long min_v=(width-1)/2;
        cout<<"Case #"<<ct<<": "<<((width-1)-min_v)<<" "<<min_v<<endl;
    }
}

