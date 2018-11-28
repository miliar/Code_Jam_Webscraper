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
    int N,P;
    cin>>N>>P;
    vi x(N);
    rep(i,0,N)cin>>x[i],x[i]%=P;    
    if(P==2){
        int z=0,o=0;
        rep(i,0,N)if(x[i])o++;else z++;
        cout<<z+(o+1)/2<<endl;
    }
    else if(P==3){
        vi cnt(P);
        rep(i,0,N)cnt[x[i]]++;
        int ans=cnt[0]+min(cnt[1],cnt[2]);
        cnt[0]=0;
        int mina=min(cnt[1],cnt[2]);
        cnt[1]-=mina;
        cnt[2]-=mina;
        ans+=(cnt[1]+2)/3+(cnt[2]+2)/3;
        cout<<ans<<endl;
    }
    else{
        vi cnt(P);
        rep(i,0,N)cnt[x[i]]++;
        int ans=cnt[0]+min(cnt[1],cnt[3])+cnt[2]/2;
        cnt[0]=0;
        int mina=min(cnt[1],cnt[3]);
        cnt[1]-=mina;
        cnt[3]-=mina;
        cnt[2]%=2;
        int otherleft=cnt[1]+cnt[3];
        if(cnt[2] and otherleft>=2){
            ans++;
            otherleft-=2;
        }
        ans+=(otherleft+3)/4;
        cout<<ans<<endl;    
    }
}

int main(){
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