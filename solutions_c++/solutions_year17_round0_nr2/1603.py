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

LL solve() {
    string s;
    cin >> s;
    int n = s.size();
    VT<int> xs(n);
    rep(i, n) xs[i] = s[i] - '0';

    // dp[digit][last number][ever under xs] = maximum 
    VVVT<LL> dp(n + 1, VVT<LL>(10, VT<LL>(2, -1)));
    dp[0][0][0] = 0;
    rep(i, n) {
        rep(j, 10) {
            rep(k, 2) {
                LL cur = dp[i][j][k];
                if (cur == -1) continue;

                for (int a = j; a < (k ? 10 : xs[i] + 1); ++a) {
                    LL next = cur * 10 + a;
                    int nk = k ? 1 : a < xs[i];
                    int nj = a;
                    MAXUD(dp[i + 1][nj][nk], next);
                }
            }
        }
    }

    LL res = 0;
    rep(j, 10) {
        rep(k, 2) {
            MAXUD(res, dp[n][j][k]);
        }
    }

    return res;
}

int main(void) {
    int t;
    cin >> t;
    rep(i, t) {
        cout << "Case #" << (i + 1) << ": " << solve() << endl;
    }

    return 0;
}

