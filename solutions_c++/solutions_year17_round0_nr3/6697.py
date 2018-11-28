#include <bits/stdc++.h>
/*#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <set>*/
#define pb push_back
#define ll long long int
#define ull unsigned long long int
#define gcd(a,b)    __gcd(a,b)
#define sz sizeof
#define INF 1000000000000000000LL
#define ms memset
#define FOR(i,N) FORR(i, 0, N)
#define FORR(i,a,b) FOTR(i, a, b, 1)
#define FOTR(i,a,b,c) for(int i=(a);i<(b);i+=(c))

using namespace std;

#define dbg(args...) {string s(#args);s+=',';cout<<"-->";debugger::call(s.begin(), s.end(), args);cout<<"\n";}
#define dbg_A(A, N) {cout<<#A<<"=(";FOR(i,N)cout<<A[i]<<" ";cout<<"\b)\n";}
struct debugger{
    typedef string::iterator si;
    static void call(si it, si ed){}
    template<typename T, typename ... aT>
    static void call(si it, si ed, T a, aT&... rest){
        string b;
        for(;*it!=',';++it) if(*it!=' ')b+=*it;
        cout << b << "=" << a << " ";
        call(++it, ed, rest...);
    }
};
ll mark[100010];
int main()
{
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    std::ios_base::sync_with_stdio(false);
    cin.tie(0);
    ll t,n,k,cases=1,l,i,j;
    cin>>t;
    while(t--){
        cin>>n>>k;
        ll mx=0;
        ms(mark,0,sz(mark));
        mark[1] = mark[n+2] = 1;
        vector<pair<ll,pair<ll,ll> > >v;
        ll ansMAX = 0, ansMIN = 1000000000,extra=0,cnk;
        for(j=1;j<=k;j++){
            v.clear();mx=0;
            ll bug=-1,dekhi=0;
            for(i=2;i<=n+1;i++){
                if(mark[i]==1){
                    extra++;
                    continue;
                }
                //left
                for(l=i;l>=1;l--){
                    if(mark[l]==1) break;
                }
                ll lidx = i-l - 1;
                //right
                for(l=i;l<=n+2;l++) if(mark[l]==1) break;
                ll ridx = l-i - 1;
                v.pb(make_pair( i, make_pair(min(lidx,ridx),max(lidx,ridx))));
                dekhi++;
                if(min(lidx,ridx)>mx){
                    mx = min(lidx,ridx);
                    bug = i;
                }
            }
            //assign

            ll asgn=bug,MX=-1;
            for(i=0;i<v.size();i++){
                if(v[i].second.first==mx){
                    if(v[i].second.second>MX){
                        MX = v[i].second.second;
                        asgn = v[i].first;
                        cnk = i;
                    }
                }
            }
            //dbg(asgn,j);
            if(asgn!=-1) mark[asgn] = 1;
        }
        /*for(i=1;i<=1000;i++){
            if(mark[i]==0) cout<<i<<endl;
        }*/
        cout<<"Case #"<<cases<<": "<<v[cnk].second.second<<" "<<v[cnk].second.first<<endl;cases++;
    }



    return 0;
}
