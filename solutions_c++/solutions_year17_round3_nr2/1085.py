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
const int N = 105;

int c[N], d[N];
int j[N], k[N];

int cao(int a0, int a1, int b0, int b1) {
    if (b1 - a0 <= 12* 60) {
        return 2;
    }
    int l = 12*60 - (a1-a0) - (b1-b0);
    int n = 5;
    if (a0+24*60-b1 <= l)
        return 2;
    return 4;
}

int go() {
    int ac, aj;
    cin>>ac>>aj;
    rp(i, ac) {
        cin>>c[i]>>d[i];
    }
    rp(i, aj) {
        cin>>j[i]>>k[i];
    }
    if (ac + aj > 2) return -1;
    if (ac+aj == 0) return 2;
    if (ac == 1 && aj == 1) {
        return 2;
    }
    if (ac == 1 && aj == 0) {
        return 2;
    }
    if (aj == 1 && ac == 0) {
        return 2;
    }
    if (ac == 2) {
        if (c[0] > c[1]) {
            swap(c[0], c[1]);
            swap(d[0], d[1]);
        }
        return cao(c[0], d[0], c[1], d[1]);
    }
    if (aj == 2) {
        if (j[0] > j[1]) {
            swap(j[0], j[1]);
            swap(k[0], k[1]);
        }
        return cao(j[0], k[0], j[1], k[1]);
    }
}

int main() {
#ifdef _TZG_DEBUG
    freopen("in.txt", "r", stdin);
#else
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int t;
    cin>>t;
    repd(_, 1, t) {
        printf("Case #%d: ", _);
        int f = go();
        printf("%d\n", f);
    }
    return 0;
}
