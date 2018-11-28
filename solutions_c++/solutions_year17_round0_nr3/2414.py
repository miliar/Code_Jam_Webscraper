#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
#define st first
#define nd second
#define pii pair<int, int>
#define pil pair<int, ll>
#define pli pair<ll, int>
#define pll pair<ll, ll>
#define pw(x) ((1LL)<<(x))
#define lson l, m, rt<<1
#define rson m+1, r, rt<<1|1
#define FIN freopen("input.txt","r",stdin);
#define FOUT freopen("output.txt","w+",stdout);
using namespace std;
/***********/
template <class T>
bool scan (T &ret) {
    char c;
    int sgn;
    if (c = getchar(), c == EOF) return 0; //EOF
    while (c != '-' && (c < '0' || c > '9') ) c = getchar();
    sgn = (c == '-') ? -1 : 1;
    ret = (c == '-') ? 0 : (c - '0');
    while (c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + (c - '0');
    ret *= sgn;
    return 1;
}
template<typename N,typename PN>inline N flo(N a,PN b){return a>=0?a/b:-((-a-1)/b)-1;}
template<typename N,typename PN>inline N cei(N a,PN b){return a>0?(a-1)/b+1:-(-a/b);}
template<typename T>
inline int sgn(T a) {return a>0?1:(a<0?-1:0);}
template <class T1, class T2>
bool gmax(T1 &a, const T2 &b) { return a < b? a = b, 1:0;}
template <class T1, class T2>
bool gmin(T1 &a, const T2 &b) { return a > b? a = b, 1:0;}

template<class A, class B, class C>
struct Triple {
    A st; B nd; C rd;
    bool operator <(const Triple &rhs) const {
        return st == rhs.st? (nd == rhs.nd? rd < rhs.rd: nd < rhs.nd): st < rhs.st;
    }
};
typedef Triple<int, int, int> tiii;

template<class T1, class T2>
ostream& operator <<(ostream &out, pair<T1, T2> p) {
    return out << "(" << p.st << ", " << p.nd << ")";
}
template<class A, class B, class C>
ostream& operator <<(ostream &out, Triple<A, B, C> t) {
    return out << "(" << t.st << ", " << t.nd << ", " << t.rd << ")";
}
template<class T>
ostream& operator <<(ostream &out, vector<T> vec) {
    out << "("; for(auto &x: vec) out << x << ", "; return out << ")";
}
const int inf = 0x3f3f3f3f;
const ll INF = 1e18;
const ll mod = 1e9+7;
const double eps = 1e-5;
const int N = 1e5+10;
/***********/
long long n, k, ans, ans1, ans2;
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("out", "w", stdout);
    int t, ca = 1; scanf("%d", &t);
    while(t--){
        printf("Case #%d: ", ca++);
        scanf("%lld%lld", &n, &k);

        map<ll, ll> ma;
        ma[n] = 1;
        for(auto it = ma.rbegin(); it != ma.rend(); it++){
            ll x = it->st, y = it->nd;
            k -= y;
            if(k <= 0) {
                ans = x;
                break ;
            }
            if(x == 1) continue ;
            if(x == 2) ma[1] += y;
            else if(x&1) ma[x/2] += y*2;
            else {
                ma[x/2] += y;
                ma[x/2-1] += y;
            }
        }
        if(ans&1) ans1 = ans2 = ans/2;
        else ans1 = ans/2, ans2 = ans1-1;
        printf("%lld %lld\n", ans1, ans2);
    }
    return 0;
}
