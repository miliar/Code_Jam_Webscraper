#include <bits/stdc++.h>

#define FORE(i, c) for (auto& i : (c))
#define FOR(i, j, k) for (int i = (j); i < (k); ++i)
#define REP(i, j) FOR(i, 0, j)
#define ALL(v) begin(v), end(v)
#define pb push_back
#define _1 first
#define _2 second
#define vec vector

using namespace std;

typedef long long ll; typedef vec<int> vi; typedef vec<ll> vll; typedef pair<ll, ll> pll; typedef pair<int, int> pii;
template <typename T, typename U> inline void amin(T& x, U y) { if (y < x) x = y; }
template <typename T, typename U> inline void amax(T& x, U y) { if (y > x) x = y; }
template <typename C, typename V> inline bool in(const C& c, const V& v) { return c.find(v) != c.end(); }
template <typename T> inline bool in(const vec<T>& v, const T& t) { return find(ALL(v), t) != end(v); }
template <typename T> inline T sq(T t) { return t * t; }

/* Debug helpers */ // FIXME: DELETE BEFORE SUBMITTING
#define TRACE(x) cout << #x _ "=" _ (x) << endl
#define _ << " " <<
#define __ << "  " <<
typedef ostream&_o;template<class T>_o _d(_o,const T&);template<class K,class V>_o operator<<(_o o,const map<K,V>&m){return
_d(o,m);}template<class T>_o operator<<(_o o,const set<T>&s){return _d(o,s);}template<class T>_o operator<<(_o o,const vec<
T>&v){return _d(o,v);}template<class A,class B>_o operator<<(_o o,const pair<A,B>&p){return o<<"{"<<p._1<<", "<<p._2<<"}";}
template<class T>_o _d(_o o,const T&v){o<<"[";int f=1;for(auto&t:v){if(!f)o<<" ";o<<t;f=0;}return o<<"]";}
/* Debug helpers */ // FIXME: DELETE BEFORE SUBMITTING
int R[55], Q[55][55], N, P;
int used[55][55];
pll Qi[55][55];

bool chk(ll a, ll b, ll c, ll d) {
    return max(a, c) <= min(b, d);
}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0);
    int T; cin >> T;
    FOR(Case, 1, T+1) {
        cin >> N >> P;
        REP(i, N) cin >> R[i];
        REP(i, N) REP(j, P) {
            cin >> Q[i][j];
            used[i][j] = 0;
        }

        bool ok = true;
        REP(i, N) REP(j, P) {
            Qi[i][j]._1 = ceil(Q[i][j] / (long double)R[i] / 1.1l - 1e-7l) + 1e-7l;
            Qi[i][j]._2 = floor(Q[i][j] / (long double)R[i] / 0.9l + 1e-7l) + 1e-7l;
            //if (Qi[i][j]._1 > Qi[i][j]._2) {
            //    ok = false;
            //    break;
            //}
            //TRACE(Qi[i][j]);
            //TRACE(Q[i][j]);
            //TRACE(R[i]);
            //assert(Qi[i][j]._1 <= Qi[i][j]._2);
        }
        //if (!ok) {
        //    cout << "Case #" << Case << ": 0\n";
        //    continue;
        //}

        REP(i, N) sort(Qi[i], Qi[i] + P, [](pll p, pll q) {
                int u =(p._2-p._1);
                int v =(q._2-q._1);
                return u < v || (u == v && p < q);
                });
        int ans = 0;
        //REP(i, N) {
        //    REP(j, P) cout << i _ j _ Qi[i][j] << endl;
        //    cout<<endl;
        //}

        REP(j, P) {
            if (Qi[0][j]._1 > Qi[0][j]._2) continue;
            ll m = Qi[0][j]._1;
            ll lo = m, hi = 1e7;
            vi last;
            bool no = true;
            while (lo < hi) {
                ll r = lo + (hi - lo) / 2;
                bool ok = true;
                vi sol;
                FOR(i, 1, N) {
                    bool found = false;
                    REP(k, P) if (!used[i][k] && Qi[i][k]._1 <= Qi[i][k]._2 && Qi[i][k]._2 <= r && chk(Qi[i][k]._1, Qi[i][k]._2, m, Qi[0][j]._2)) {
                        sol.pb(k);
                        found = true;
                        break;
                    }
                    if (!found) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    last = sol;
                    hi = r;
                    no = false;
                } else
                    lo = r + 1;
                sol.clear();
            }
            if (!no) {
            //cout << j _ m __ lo _ hi __ last;
                assert(last.size() == N-1);
                ++ans;
                int i = 1;
                FORE(x, last)
                    used[i++][x] = 1;
            }
        }

        //int ans = 0;
        //FOR(s, 1, 1e6+5) {
        //    bool ok = true;
        //    vi sol;
        //    REP(i, N) {
        //        bool found = false;
        //        REP(j, P) if (!used[i][j] && Qi[i][j]._1 <= s && Qi[i][j]._2 >= s) {
        //            sol.pb(j);
        //            found = true;
        //            break;
        //        }
        //        if (!found) {
        //            ok = false;
        //            break;
        //        }
        //    }

        //    if (!ok) continue;
        //    assert(sol.size() == N);
        //    ++ans;
        //    int i = 0;
        //    FORE(x, sol)
        //        used[i++][x] = s;
        //    --s;
        //}
        cout << "Case #" << Case << ": " << ans << endl;
    }
    return 0;
}

