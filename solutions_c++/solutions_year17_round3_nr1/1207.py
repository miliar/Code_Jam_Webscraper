#include <iostream>
#include <cstdlib>
#include <cctype>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cassert>
#include <bitset>
#include <functional>
using namespace std;
#define RI(X) scanf("%d", &(X))
#define RLL(X) scanf("%lld", &(X))
#define DRI(X) int (X); scanf("%d", &X)
#define rep(i,a,n) for(int i=(a);i<(int)(n);i++)
#define repd(i,a,b) for(int i=(a);i>=(b);i--)
#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define MP make_pair
#define PB push_back
#define AA first
#define BB second
#define OP begin()
#define ED end()
#define SZ size()
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<PII> VPII;
typedef vector<PLL> VPLL;
#define cmin(x,y) x=min(x,y)
#define cmax(x,y) x=max(x,y)
const LL MOD = 1000000007;
const double PI = acos(-1.);
const double eps = 1e-9;
LL modPow(LL a,LL b,LL MOD){
    LL ret=1;for(;b;b>>=1){
        if(b&1)ret=ret*a%MOD;
        a=a*a%MOD;
    }return ret;
}

const int MXN = 1005;
int n, x;

struct pan
{
    LL r, h;
    bool operator < (const pan& x) const {
        return r * h == x.r * x.h ? r > x.r : r * h > x.r * x.h;
    }
} PAN[MXN];
void solve() {
    DRI(N);
    DRI(K);
    LL ans1 = 0LL, maxr = 0LL;
    rep(i,0,N){
        RLL(PAN[i].r); RLL(PAN[i].h);
    }
    sort(PAN, PAN+N);
    
    rep(i,0,K-1){
        //printf("%lld %lld\n", PAN[i].r,PAN[i].h);
        ans1 += PAN[i].r*PAN[i].h*2;
        cmax(maxr, PAN[i].r);
    }
    LL ans2 = 0LL;
    rep(i,K,N){
        LL curR = max(maxr, PAN[i].r);
        if(max(maxr, PAN[K-1].r)*max(maxr, PAN[K-1].r) + PAN[K-1].r*PAN[K-1].h*2 < 
            curR*curR + PAN[i].r*PAN[i].h*2){
            ans2 = max(ans2, curR*curR + PAN[i].r*PAN[i].h*2);
        }
    }
    if (ans2 == 0LL){
        ans1 += max(maxr, PAN[K-1].r)*max(maxr, PAN[K-1].r) + PAN[K-1].r*PAN[K-1].h*2;
    } else {
        ans1 += ans2;
    }
    printf("%.9f\n", ans1 * PI);
    // cout<<ans<<"\n";
}

int main(int argc, char const *argv[]) {
    int _T=1;
    scanf("%d",&_T);
    rep(CA,0,_T){
        printf("Case #%d: ",CA+1);
        solve();
    }
    return 0;
}
