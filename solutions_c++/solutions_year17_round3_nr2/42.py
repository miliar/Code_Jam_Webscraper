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
    int AC,AJ;
    cin>>AC>>AJ;
    int N=AC+AJ;
    vector<pair<pii,int>>v(AC+AJ);
    int ACcnt=0,AJcnt=0,othercnt=0,ACmid=0,AJmid=0;
    vi AJs,ACs;
    rep(i,0,AC){
        cin>>v[i].F.F>>v[i].F.S;
        v[i].S=1;
        ACcnt+=v[i].F.S-v[i].F.F;
    }
    rep(i,0,AJ){
        cin>>v[AC+i].F.F>>v[AC+i].F.S;
        v[AC+i].S=2;
        AJcnt+=v[AC+i].F.S-v[AC+i].F.F;
    }
    sort(all(v));
    int ans=0;
    rep(i,0,N){
        auto x=v[i];
        auto y=v[(i+1)%N];
        if(y.F.F<x.F.S)y.F.F+=1440,y.F.S+=1440;
        if(x.S!=y.S){
            othercnt+=(y.F.F-x.F.S);
            ans++;
        }
        else if(x.S==1){
            ACmid+=(y.F.F-x.F.S);
            ACs.pb(y.F.F-x.F.S);
        }
        else{
            AJmid+=(y.F.F-x.F.S);
            AJs.pb(y.F.F-x.F.S);
        }
    }

    sort(all(ACs),greater<int>());
    sort(all(AJs),greater<int>());
    if(ACcnt+othercnt+ACmid>=720 and AJcnt+othercnt+AJmid>=720){
        cout<<ans<<endl;
        return;
    }
    if(ACcnt+othercnt+ACmid<720){
        int reqd=720-(ACcnt+othercnt+ACmid);
        for(auto i:AJs){
            if(reqd>0)reqd-=i,ans+=2;
        }
        cout<<ans<<endl;
        return;
    }
    if(AJcnt+othercnt+AJmid<720){
        int reqd=720-(AJcnt+othercnt+AJmid);
        for(auto i:ACs){
            if(reqd>0)reqd-=i,ans+=2;
        }
        cout<<ans<<endl;
        return;
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