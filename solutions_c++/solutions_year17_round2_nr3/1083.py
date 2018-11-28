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
using namespace std;

int test=1;
void solve(){
    cout<<"Case #"<<test++<<": ";
    int N,Q;
    cin>>N>>Q;
    vector<pii>x(N+1);
    rep(i,1,N+1)cin>>x[i].F>>x[i].S;
    int d[N+1][N+1];
    rep(i,1,N+1){
        rep(j,1,N+1)cin>>d[i][j];
    }
    while(Q--){
        int u,v;
        cin>>u>>v;
        long double dp[N+1];
        rep(i,0,N+1)dp[i]=1e20;
        dp[1]=0;
        rep(i,2,N+1){
            int distance=0;
            for(int j=i-1;j>=1;j--){
                distance+=d[j][j+1];
                if(x[j].F>=distance)dp[i]=min(dp[i],dp[j]+distance*1.0l/x[j].S);
            }
        }
        cout<<fixed<<setprecision(8)<<dp[N]<<endl;
    }
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