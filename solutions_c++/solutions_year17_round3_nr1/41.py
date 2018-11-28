#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>

#ifdef PRINTERS
#include "printers.hpp"
using namespace printers;
#define tr(a)        cerr<<#a<<": "<<a<<endl;
#else
#define tr(a)    
#endif
#define int         long long
#define ll          long long
#define pb          push_back
#define mp          make_pair
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define sz(x)       (int)x.size()
#define hell        1000000007
#define endl        '\n'
#define rep(i,a,b)    for(int i=a;i<b;i++)
#define PI          3.141592653589793l
using namespace std;
int test=1;
void solve(){
    cout<<"Case #"<<test++<<": ";
    int N,K;
    cin>>N>>K;
    vector<pii>x(N);
    //H,R sorted by H*R, decreasing
    rep(i,0,N)cin>>x[i].S>>x[i].F,x[i].F*=x[i].S;
    sort(all(x));
    reverse(all(x));
    long double curmax=0;
    rep(i,0,N){
        int left=K-1;
        int R=x[i].S;
        int H=x[i].F;
        rep(j,0,N){
            if(i==j or x[j].S>x[i].S)continue;
            if(!left)continue;
            H+=x[j].F;
            left--;
        }
        if(left)continue;
        curmax=max(curmax,1.0l*PI*R*R+2*PI*H);
    }
    cout<<fixed<<setprecision(10)<<curmax<<endl;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t=1;
    cin>>t;
    while(t--){
        solve();
    }
    return 0;
}