#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(a),__tzg_##i=(b);i<__tzg_##i;++i)
#define urp(i,a,b) for(int i=(a),__tzg_##i=(b);i>=__tzg_##i;--i)
#define rp(i,b) rep(i,0,b)
#define repd(i,a,b) rep(i,a,(b)+1)
#define mst(a,b) memset(a,b,sizeof(a))
#define vrp(it,v) for(auto it(v.begin());(it)!=(v.end());++it)
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
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;

const int N = 2005;

void gao(){
    string _s;
    VI s;
    int k;
    int cnt = 0;
    cin>>_s>>k;
    rp(i, siz(_s)) s.pb(_s[i]=='+'?1:-1);
    rep(i, 0, siz(s)) {
        if (s[i] == 1) {
            continue;
        } else {
            if (siz(s)-i < k) {
                puts("IMPOSSIBLE");
                return ;
            }
            rep(j, i, i+k) {
                s[j] = -s[j];
            }
            ++cnt;
        }
    }
    printf("%d\n", cnt);
}

int main() {
#ifdef _TZG_DEBUG
    freopen("in.txt", "r", stdin);
#else
    freopen("A-large.in", "r", stdin);
    freopen("a.txt", "w", stdout);
#endif
    int _;
    cin>>_;
    repd(i, 1, _){
        printf("Case #%d: ", i);
        gao();
    }
    return 0;
}
