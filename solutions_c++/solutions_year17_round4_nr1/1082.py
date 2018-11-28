//marico el que lo lea
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

#define FOR(i,f,t) for(int i=f; i<(int)t; i++)
#define FORR(i,f,t) for(int i=f; i>(int)t; i--)
#define pb push_back
#define ms(obj, val) memset(obj, val, sizeof(obj))
#define ms2(obj, val, sz) memset(obj, val, sizeof(obj[0])*sz)
#define ri(x) scanf("%d",&x)
#define rl(x) scanf("%lld",&x)
#define rii(x,y) ri(x), ri(y)

#define fst first
#define snd second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;

const int MAXN = 102;

int N, P;
        //1     2     3
int dp[MAXN][MAXN][MAXN];
int f(int r1, int r2, int r3, int rr){
    if(r1==0 && r2 ==0 && r3==0) return 0;
    int &ret = dp[r1][r2][r3];
    if(ret!=-1) return ret;
    ret = 0;
    if(r1) ret = max(ret, f(r1-1, r2, r3, (rr-1+P)%P));
    if(r2) ret = max(ret, f(r1, r2-1, r3, (rr-2+P)%P));
    if(r3) ret = max(ret, f(r1, r2, r3-1, (rr-3+P)%P));
    if(rr==0) ret++;
    return ret;
}

int r[5];
int main(){
    int TC; ri(TC);
    FOR(tc,1,TC+1){
        rii(N, P);
        ms(r,0);
        FOR(i,0,N){
            int G; ri(G);
            r[G%P]++;
        }
        ms(dp, -1);
        printf("Case #%d: %d\n",tc,r[0]+f(r[1],r[2],r[3],0));
    }
}
