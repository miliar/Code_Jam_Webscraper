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


int k[1222], s[1222];
double ti[1222];
bool test(double x, vector<pii> &ve, int n){
    for(int i = 0; i < n; i++)
        if(x > ve[i].nd){
            if(ve[i].st*1.0/(x-ve[i].nd) < ti[i])
                return false;
        }
    return true;
}
int main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t, ca = 1; cin >> t;
    vector<pii> ve;

    while(t--){
        printf("Case #%d: ", ca++);
        ve.clear();
        vector<pii> tmp;
        int d, n, k, s;
        cin >> d >> n;
        for(int i = 0; i < n; i++){
            cin >> k >> s;
            tmp.push_back({k, s});
        }
        sort(tmp.begin(), tmp.end());
        ve.push_back(tmp[0]);
        for(int i = 1; i < n; i++){
            pii last = ve[ ve.size()-1 ];
            if(tmp[i].nd >= last.nd) continue ;
            ve.push_back(tmp[i]);
        }
        n = ve.size();

//        if(ca == 96){
//            cout << "gg" << endl;
//            cout << d << endl;
//            for(int i = 0; i < ve.size(); i++)
//                cout << ve[i].st << ' ' << ve[i].nd << endl;
//            //return 0;
//        }

        for(int i = n-1; i >= 0; i--){
            ti[i] = (d-ve[i].st)*1.0/ve[i].nd;
            for(int j = i+1; j < n; j++)
                ti[i] = min(ti[i], (ve[j].st-ve[i].st)*1.0/(ve[i].nd-ve[j].nd));
        }


        double l = 0, r = d/ti[n-1]+5, ans = 0;
        for(int i = 0; i < 100; i++){
            double m = (l+r)*0.5;
            if(test(m, ve, n))
                ans = m, l = m;
            else
                r = m;
        }
        printf("%.20f\n", ans);
        //if(ca == 68) return 0;
    }
    return 0;
}
