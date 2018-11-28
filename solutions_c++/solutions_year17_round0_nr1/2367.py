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
int c[2010], d[2010];
string s;
int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out", "w", stdout);
    int t, k, ca = 1; cin >> t;
    while(t--){
        cin >> s >> k;
        int ans = 0, sum = 0;
        for(int i = 0; i < s.size(); i++)
            c[i] = s[i] == '-', d[i] = 0;
        for(int i = 0; i < s.size(); i++){
            if(i) d[i] ^= d[i-1];
            if(i+k <= s.size()){
                if(c[i]^d[i]){
                    ans++;
                    d[i] ^= 1, d[i+k] ^= 1;
                }
            }

        }
        bool tag = true;
        for(int i = 0; i < s.size(); i++)
            if(c[i]^d[i]) tag = false;
        printf("Case #%d: ", ca++);
        if(tag) printf("%d\n", ans);
        else puts("IMPOSSIBLE");
    }

    return 0;
}
