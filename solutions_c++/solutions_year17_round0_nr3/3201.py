#include<iostream>
#include <limits>
#include <algorithm>
#include<vector>
#include<iomanip>
#include<string>
#include<unordered_map>
#include<stack>
#include <queue>
#include <deque>
#include <chrono>
#include <math.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <random>
#define forn(i,n) for(int i=0;i<n;++i)
#define mp std::make_pair
#define pii std::pair<int, int>
#define pll std::pair<long long, long long>
using std::cin;
using std::cout;

int main(){
    int T;
    long long n,k;
    std::queue<pll > qu,empt;
    cin>>T;
    long long st, en;
    long long mid;
    forn(i,T){
        cin>>n>>k;
        st=0;
        en=n-1;
        while(k>1){
            mid=st+(en-st)/2;
            k--;
            if(k%2==0){
                en=mid-1;
                k/=2;
            }else{
                st=mid+1;
                k=(k+1)/2;
            }
        }
        //cout<<st<<" "<<en<<"\n";
        mid=st+(en-st)/2;
        //cout<<mid<<"\n";
        cout<<"Case #"<<i+1<<": " ;
        cout<<std::max(mid-st,en-mid)<<" ";
        cout<<std::min(mid-st,en-mid)<<"\n";

    }
    return 0;
}
