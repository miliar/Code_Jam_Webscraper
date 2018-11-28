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


int C, J;
VT<PII> cs, js;

void dump1() {
    cout << "C " << C << endl;
    for (auto &c : cs) {
        int s = c.fst;
        int e = c.snd;
        cout << (s / 60) << ":" << (s % 60);
        cout << " - ";
        cout << (e / 60) << ":" << (e % 60) << endl;
    }
    cout << "J " << J << endl;
    for (auto &j : js) {
        int s = j.fst;
        int e = j.snd;
        cout << (s / 60) << ":" << (s % 60);
        cout << " - ";
        cout << (e / 60) << ":" << (e % 60) << endl;
    }
    puts("");
}

int solve() {
    cin >> C >> J;
    cs = VT<PII>(C);
    js = VT<PII>(J);
    rep(i, C) cin >> cs[i].fst >> cs[i].snd;
    rep(i, J) cin >> js[i].fst >> js[i].snd;
    sort(ALL(cs));
    sort(ALL(js));

    // offset time
    int min_t = INF;
    rep(i, C) MINUD(min_t, cs[i].fst);
    rep(i, J) MINUD(min_t, js[i].fst);
    rep(i, C) {
        cs[i].fst -= min_t;
        cs[i].snd -= min_t;
    }
    rep(i, J) {
        js[i].fst -= min_t;
        js[i].snd -= min_t;
    }

//    DUMP1();

    VT<int> as(1440 + 1, -1);
    for (auto &c : cs) REP(i, c.fst, c.snd) as[i] = 0;
    for (auto &j : js) REP(i, j.fst, j.snd) as[i] = 1;

    int ans = INF;
    
    rep(first, 2) {
        VVVT<int> dp(1440 + 1, VVT<int>(1440 + 1, VT<int>(2, INF)));
        dp[0][0][first] = 0;

        rep(ti, 1440) {
            rep(cwork, 1440) {
                rep(who, 2) {
                    int cur = dp[ti][cwork][who];
                    if (cur == INF) continue;

                    // nochange
                    if (as[ti] != who) {
                        MINUD(dp[ti + 1][cwork + who][who], cur);
                    }

                    // change
                    int nw = who ? 0 : 1;
                    if (as[ti] != nw) {
                        MINUD(dp[ti + 1][cwork + nw][nw], cur + 1);
                    }
                }
            }
        }

        MINUD(ans, dp[1440][720][!first] + 1);
        MINUD(ans, dp[1440][720][first]);
    }

    return ans;
}

int main(void) {
    int t;
    cin >> t;
    rep(i, t) {
        printf("Case #%d: %d\n", i + 1, solve());
    }

    return 0;
}

