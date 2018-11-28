#include <bits/stdc++.h>
using namespace std;

typedef ostringstream OSS; typedef istringstream ISS;
typedef long long LL;
typedef unsigned int  UI;
typedef pair<int, int> PII;  typedef pair<LL, LL> PLL;

template <typename T> using VT = vector<T>;
template <typename T> using VVT = VT<VT<T>>;
template <typename T> using VVVT = VT<VT<VT<T>>>;
template <typename T> using VVVVT = VT<VT<VT<VT<T>>>>;

#define fst first
#define snd second
#define MP make_pair
#define PB push_back
#define EB emplace_back 
#define ALL(x)  (x).begin(),(x).end()
#define RALL(x) (x).rbegin(),(x).rend()
#define RANGEBOX(x,y,maxX,maxY) (0 <= (x) && 0 <= (y) && (x) < (maxX) && (y) < (maxY))
#define RANGE(x, l, r) ((l) <= (x) && (x) <= (r))
#define rep(i, N)  for (int i = 0; i < (int)(N); i++)
#define rrep(i, N) for (int i = N - 1; i >= 0; i--)
#define REP(i, init, N)  for (int i = (init); i < (int)(N); i++)
#define RREP(i, N, last) for (int i = (init - 1); i >= last; i--)
#define MAXUD(orig, target) orig = max(orig, target)
#define MINUD(orig, target) orig = min(orig, target)
#define DUMP(x) cerr << #x << " = " << (x) << endl

template < typename T > inline T fromString(const string &s) { T res; ISS iss(s); iss >> res; return res; };
template < typename T > inline string toString(const T &a)   { OSS oss; oss << a; return oss.str(); };

template<typename T=int> inline void dump(vector<T> vs, bool ent=false) { rep(i, vs.size()) cout << vs[i] << (i+1==vs.size() ? '\n' : ' '); if (ent) cout << endl; }
template<typename T = int> inline void dump(vector<vector<T>> vs, bool ent=false) { rep(i, vs.size()) dump<T>(vs[i]); if (ent) cout << endl; }

const int    INF  = 0x3f3f3f3f;
const LL     INFL = 0x3f3f3f3f3f3f3f3fLL;
const double DINF = 0x3f3f3f3f;
const int    DX[] = {1,  0, -1, 0};
const int    DY[] = {0, -1,  0, 1};
const double EPS  = 1e-12;
// const double PI   = acos(-1.0);

template<typename T = int> inline T in() { T x; cin >> x; return x; }
template<typename T = int> inline vector<T> in(int n) { vector<T> xs(n); rep(i, n) cin >> xs[i]; return xs; }
template<typename T = int> inline vector<vector<T>> in(int n, int m) { vector<vector<T>> xs(n, vector<T>(m)); rep(i, n) rep(j, m) cin >> xs[i][j]; return xs; }

PII solve() {
    int n, c, m;
    cin >> n >> c >> m;
    assert(c == 2);
    VVT<int> ts(2);
    rep(i, m) {
        int p, b;
        cin >> p >> b;
        ts[b - 1].PB(p);
    }

    rep(i, 2){
        sort(ALL(ts[i]));
    }

    int m0 = ts[0].size();
    int m1 = ts[1].size();

    if (!m0 || !m1) return MP(max(m0, m1), 0);

    PII ans(INF, INF);

    rep(i, m1) {
        int i0 = 0, i1 = 0;
        PII tmp;

        while (i0 != m0 && i1 != m1) {
            int a = ts[0][i0];
            int b = ts[1][(i1 + i) % m1];
            
            if (a == b) {
                if (a == 1) {
                    tmp.fst += 2;
                } else {
                    tmp.fst += 1;
                    tmp.snd += 1;
                }
            } else {
                tmp.fst += 1;
            }
            ++i0;
            ++i1;
        }

        tmp.fst += m0 - i0;
        tmp.fst += m1 - i1;

        MINUD(ans, tmp);
    }
    
    return ans;
}

int main(void) {
    int t;
    cin >> t;
    rep(i, t) {
        PII ans = solve();
        printf("Case #%d: %d %d\n", i + 1, ans.fst, ans.snd);
    }

    return 0;
}

