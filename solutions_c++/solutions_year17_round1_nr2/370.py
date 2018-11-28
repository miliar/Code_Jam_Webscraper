//marico el que lo lea
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
using namespace std;

#define FOR(i,f,t) for(int i=f;i<(int)t; i++)
#define FORR(i,f,t) for(int i=f;i>(int)t; i--)
#define ms(obj, val) memset(obj, val, sizeof(obj))
#define ms2(obj, val, sz) memset(obj, val, sizeof(obj[0])*sz)
#define pb push_back
#define ri(x) scanf("%d",&x)
#define rii(x,y) ri(x), ri(y)

typedef vector<int> vi;
typedef long long ll;

const int MAXN = 52, MAXP = 52;

int N, K;
int R[MAXN];
int P[MAXN][MAXP];

vector<int> av[MAXN];

int find_mn_sngs(ll x, ll r){
    ll lo = 1, hi = 2e6+6;
    while(lo < hi){
        ll k = (lo + hi)/2;
        if(r*k*9 <= x*10 && r*11*k >= x*10) hi=k;
        if(r*k*9 > x*10) hi = k-1;
        if(r*11*k < x*10) lo = k+1;
    }
    if(lo>0 && r*9*lo <= x*10 && r*11*lo >= x*10) return (int)lo;
    if(hi>0 && r*9*hi <= x*10 && r*11*hi >= x*10) return (int)hi;
    return -1;
}
int find_mx_sngs(ll x, ll r){
    ll lo = 1, hi = 2e6+6;
    while(lo < hi){
        ll k = (lo + hi +1)/2;
        if(r*k*9 <= x*10 && r*11*k >= x*10) lo=k;
        if(r*k*9 > x*10) hi = k-1;
        if(r*11*k < x*10) lo = k+1;
    }
    if(lo>0 && r*9*lo <= x*10 && r*11*lo >= x*10) return (int)lo;
    if(hi>0 && r*9*hi <= x*10 && r*11*hi >= x*10) return (int)hi;
    return -1;
}

int main(){
    int TC; ri(TC);
    FOR(tc,1,TC+1){
        rii(N,K);
        FOR(i,0,N) av[i].clear();
        FOR(i,0,N) ri(R[i]);
        FOR(i,0,N) FOR(j,0,K) ri(P[i][j]);
        FOR(i,0,N) FOR(j,0,K) av[i].pb(P[i][j]);
        FOR(i,0,N) sort(av[i].begin(), av[i].end(), greater<int>());
        int ans = 0;
        while(true){
            bool good = true;
            FOR(i,0,N) if(av[i].size() == 0) good = false;
            if(!good) break;
            int mnmx = find_mx_sngs(av[0].back(), R[0]);
            int mxmn = find_mn_sngs(av[0].back(), R[0]);
            FOR(i,1,N){
                mnmx = min(mnmx, find_mx_sngs(av[i].back(), R[i]));
                mxmn = max(mxmn, find_mn_sngs(av[i].back(), R[i]));
            }
            if(mnmx != -1 && mxmn != -1 && mxmn <= mnmx){
                ans ++;
                FOR(i,0,N) av[i].pop_back();
            }else{
                int mn = av[0].back();
                FOR(i,1,N) mn = min(mn, av[i].back());
                FOR(i,0,N) if(av[i].back() == mn) av[i].pop_back();
            }
        }
        printf("Case #%d: %d\n",tc,ans);
    }
}
