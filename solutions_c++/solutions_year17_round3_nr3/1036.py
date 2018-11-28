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
#define RD(X) scanf("%lf", &(X))
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

const int MXN = 105;

void solve() {
    DRI(N);
    DRI(K);
    double U, sum = 0;
    RD(U);
    double p[N];
    rep(i,0,N){
        RD(p[i]);
        sum += p[i];
    }
    double ans = 1.0;
    if(sum + U < N) {
        sort(p,p+N);
        int n = N;
        double base = 0.0;
        while(n>=1){
            base = (sum + U) / n;
            if(base>=p[n-1]){
                break;
            }
            --n;
            sum -= p[n];
        }
        base = (sum + U) / n;
        rep(i,0,n){
            ans *= base;
        }
        rep(i,n,N){
            ans *= p[i];
        }
    }
    printf("%.6f\n", ans);
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
