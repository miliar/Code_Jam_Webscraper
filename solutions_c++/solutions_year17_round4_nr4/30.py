#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define fore(i, b, e) for (int i = (int)(b); i <= (int)(e); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define pb push_back
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
typedef long long ll;

#define prev asd

const int maxn = 30;
const int K = 10;

int n, m, lim, nt, ns;
char c[maxn][maxn];
int tid[maxn][maxn];
int sid[maxn][maxn];
int d[maxn][maxn];
int tur[maxn][maxn];
vector<pii> ss, tt;
bool can[maxn][maxn][1<<K];

int dp[1<<K][1<<K];
pii prev[1<<K][1<<K];

const int dx[] = {0, 0, 1, -1};
const int dy[] = {1, -1, 0, 0};

void mark(int x, int y, int col) {
    tur[x][y] |= 1<<col;
    forn(i, 4) {
        int xx = x, yy = y;
        while (true) {
            xx += dx[i];
            yy += dy[i];
            if (xx < 0 || yy < 0 || xx >= n || yy >= m || c[xx][yy] == '#') break;
            tur[xx][yy] |= 1<<col;
        }
    }
}

void dfs(int sx, int sy, int mask) {
    memset(d, -1, sizeof d);
    d[sx][sy] = 0;
    vector<pii> q{{sx, sy}};
    forn(III, q.size()) {
        int x, y;
        tie(x, y) = q[III];
        forn(i, 4) {
            int xx = x+dx[i], yy = y+dy[i];
            if (xx < 0 || yy < 0 || xx >= n || yy >= m || c[xx][yy] == '#') continue;
            if (d[xx][yy] != -1) continue;
            bool can = 1;
            forn(i, nt) if (!(mask&(1<<i))) {
                if ( (tur[x][y] & (1<<i)) ) {
                    can = false;
                }
            }
            if (can) {
                d[xx][yy] = d[x][y] + 1;
                q.pb({xx, yy});
            }
        }
    }
}

void solve(int tn) {
    memset(tid, -1, sizeof tid);
    memset(sid, -1, sizeof sid);
    memset(tur, 0, sizeof tur);
    memset(can, 0, sizeof can);
    ss.clear();
    tt.clear();

    cin >> m >> n >> lim;
    nt = ns = 0;
    forn(i, n) cin >> c[i];
    forn(i, n) forn(j, m) {
        if (c[i][j] == 'T') {
            tt.pb({i, j});
            tid[i][j] = nt++;
        }
        if (c[i][j] == 'S') {
            ss.pb({i, j});
            sid[i][j] = ns++;
        }
    }
    forn(i, nt) mark(tt[i].fi, tt[i].se, i);
    forn(s, ns) forn(mask, 1<<nt) {
        dfs(ss[s].fi, ss[s].se, mask);
        /*
        if (s == 2 && mask == (1<<1)) {
            forn(i, n) {
                forn(j, m) cerr << d[i][j] << " ";
                cerr << endl;
            }
            cerr << endl;
        }
        */
        forn(i, n) forn(j, m) if (d[i][j] != -1 && d[i][j] <= lim) {
            forn(tt, nt) if (!(mask&(1<<tt))) if (tur[i][j] & (1<<tt)) {
                can[s][tt][mask] = 1;
//                 cerr << "can " << s << " " << tt << " " << mask << endl;
            }
        }
    }

    memset(dp, 0, sizeof dp);
    dp[0][0] = 1;
    pii best(0, 0);
//     cerr << ns << " " << nt << endl;
    forn(ms, 1<<ns) forn(mt, 1<<nt) if (dp[ms][mt]) {
        int b = __builtin_popcount(ms);
        if (__builtin_popcount(best.fi) < b) {
            best = {ms, mt};
        }
        forn(s, ns) if (!(ms&(1<<s))) {
            forn(t, nt) if (!(mt&(1<<t))) {
                if (can[s][t][mt]) {
                    int ns = ms|(1<<s);
                    int nt = mt|(1<<t);
                    dp[ns][nt] = 1;
                    prev[ns][nt] = {s, t};
                }
            }
        }
    }
    int ms, mt;
    tie(ms, mt) = best;
    vector<pii> res;
    while (ms) {
        int s, t;
        tie(s, t) = prev[ms][mt];
        res.pb({s, t});
        ms ^= 1<<s;
        mt ^= 1<<t;
    }
    reverse(all(res));
    cout << "Case #" << tn << ": " << res.size() << "\n";
    for (auto x: res) cout << x.fi+1 << " " << x.se+1 << "\n";
}

int main() {
#ifdef LOCAL
//     freopen("d.in", "r", stdin);
#endif

    int t;
    cin >> t;
    forn(i, t) {
        solve(i+1);
    }


#ifdef LOCAL
    cerr << "Time elapsed: " << clock() / 1000 << " ms" << endl;
#endif
    return 0;
}
