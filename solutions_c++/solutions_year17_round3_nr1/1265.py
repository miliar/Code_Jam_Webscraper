#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(a),__tzg_##i=(b);i<__tzg_##i;++i)
#define urp(i,a,b) for(int i=(a),__tzg_##i=(b);i>=__tzg_##i;--i)
#define rp(i,b) rep(i,0,b)
#define repd(i,a,b) rep(i,a,(b)+1)
#define mst(a,b) memset(a,b,sizeof(a))
#define vtr(v) (v).begin(),(v).end()
#define mp(a,b) make_pair(a,b)
#define fi first
#define se second
#define pb(a) push_back(a)
#define _0(x) (!(x))
#define _1(x) (x)
#define bit(x,y) (((x)>>(y))&1)
#define siz(x) ((int)(x).size())
template<typename T>inline void smin(T & x, const T &y) {
    x=min(x,y);
}
template<typename T>inline void smax(T & x, const T &y) {
    x=max(x,y);
}

typedef long long LL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long double ld;
const int N = 1005;
const ld pi = (ld)acos(-1.0);
ld dp[N][N];
struct node{
    ld r, h;
    ld v, o;
    bool operator < (const node & a) const {
        return r < a.r;
    }
    void build() {
        v = 2.0*pi*r*h;
        o = r*r*pi;
    }
} da[N];

ld go() {
    int n, k;
    cin>>n>>k;
    rp(i, n){
        cin>>da[i].r>>da[i].h;
        da[i].build();
    }
    sort(da, da+n);
    repd(kk, 1, k) {
        repd(nn, 0, n-1) {
            dp[kk][nn] = da[nn].o + da[nn].v;
            repd(i, 0, nn-1) {
                smax(dp[kk][nn], dp[kk-1][i]+da[nn].v+(da[nn].o - da[i].o));
            }
        }
    }
    ld ans = 0.0;
    repd(i, 0, n-1) smax(ans, dp[k][i]);
    return ans;
}

int main() {
#ifdef _TZG_DEBUG
    freopen("in.txt", "r", stdin);
#else
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int t;
    cin>>t;
    repd(_, 1, t) {
        printf("Case #%d: ", _);
        double f = go();
        printf("%.8lf\n", f);
    }
    return 0;
}
