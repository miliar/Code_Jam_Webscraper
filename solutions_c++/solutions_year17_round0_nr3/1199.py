#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <set>
#include <numeric>
#include <cmath>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <queue>
#include <numeric>
#include <iomanip>
#define ll long long
using namespace std;
ll testCase;
map<ll,ll> mp;
long long n,k;
int main(){
    ios::sync_with_stdio(false);
    
    freopen("/Users/papaya0033/Desktop/C-small-1-attempt0.in","r",stdin);
    freopen("/Users/papaya0033/Desktop/C-small-1-attempt0.out","w",stdout);
    cin>>testCase;
    for(ll t=1;t<=testCase;t++){
        mp.clear();
        cin>>n>>k;
        mp[n]=1;
        long long y=0;long long z=0;
        while(k){
            auto mx=mp.rbegin()->first;
            auto cnt=mp.rbegin()->second;
            if(cnt<=k){
                k-=cnt;
                mp.erase(mp.rbegin()->first);
            }
            else{
                k=0;
            }
            if(mx&1){
                y=mx/2;
                z=mx/2;
                mp[y]+=cnt;
                mp[z]+=cnt;
            }
            else{
                y=mx/2;
                z=mx/2-1;
                mp[y]+=cnt;
                mp[z]+=cnt;
            }
        }
        cout<<"Case #"<<t<<": "<<y<<" "<<z<<"\n";
    }
    
    return 0;
}
