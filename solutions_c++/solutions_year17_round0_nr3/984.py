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

LL gao() {
    LL n, k;
    cin>>n>>k;
    --k;
    map<LL, LL> mmp;
    mmp[n] = 1;
    while (k) {
        auto it = --mmp.end();
        LL a = it->fi, b = it->se, c = min(b, k);
        it->se -= c;
        k -= c;
        if (it->se == 0) {
            mmp.erase(it);
        }
        --a;
        LL ra = a/2, rb = a - ra;
        mmp[ra]+=c;
        mmp[rb]+=c;
    }
    auto it = mmp.end();
    it--;
    LL ra = (it->fi-1)/2, rb = it->fi-1 - ra;
    cout<<rb<<" "<<ra<<endl;
}

int main() {
#ifdef _TZG_DEBUG
    freopen("in.txt", "r", stdin);
#else
    freopen("C-large.in", "r", stdin);
    freopen("c.large.txt", "w", stdout);
#endif
    int _;
    cin>>_;
    repd(i, 1, _) {
        printf("Case #%d: ", i);
        gao();
    }
    return 0;
}
