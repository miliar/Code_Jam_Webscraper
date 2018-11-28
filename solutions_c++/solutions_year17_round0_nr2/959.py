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
template<typename T>inline void smin(T & x, const T &y) {x=min(x,y);}
template<typename T>inline void smax(T & x, const T &y) {x=max(x,y);}
typedef long long LL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

const int N = 2005;

LL gao(){
    LL n;
    cin>>n;
    VLL x;
    {
        LL m = n;
        while (m){
            x.pb(m % 10);
            m /= 10;
        }
    }
    reverse(vtr(x));
    int o = -1;
    rep(i, 1, siz(x)){
        if (x[i-1] > x[i]) {
            o = i-1;
            break;
        }
    }
    if (o == -1) return n;
    int u = x[o]-1;
    int p = -1;
    urp(i, o-1, 0){
        if (x[i] <= u) {
            p = i;
            break;
        }
    }
    x[p+1]--;
    rep(i, p+2, siz(x)) x[i] = 9;
    LL res = 0;
    rp(i, siz(x)) res = res * 10, res += x[i];
    return res;
}

int main() {
#ifdef _TZG_DEBUG
    freopen("in.txt", "r", stdin);
#else
    freopen("B-large.in", "r", stdin);
    freopen("b.txt", "w", stdout);
#endif
    int _;
    cin>>_;
    repd(i, 1, _){
        printf("Case #%d: ", i);
        cout<<gao()<<endl;
    }
    return 0;
}
