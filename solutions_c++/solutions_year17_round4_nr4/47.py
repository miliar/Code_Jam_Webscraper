#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define nfor(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i < int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pti;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

template<typename A, typename B> inline ostream& operator<< (ostream& out, const pair<A, B>& p) { return out << "(" << p.x << ", " << p.y << ")"; }
template<typename T> inline ostream& operator<< (ostream& out, const vector<T>& a) { out << "["; forn(i, sz(a)) { if (i) out << ','; out << ' ' << a[i]; } return out << " ]"; } 
template<typename T> inline ostream& operator<< (ostream& out, const set<T>& a) { return out << vector<T>(all(a)); }
template<typename X, typename Y> inline ostream& operator<< (ostream& out, const map<X, Y>& a) { return out << vector<pair<X, Y>>(all(a)); }
template<typename T> inline ostream& operator<< (ostream& out, pair<T*, int> a) { return out << vector<T>(a.x, a.x + a.y); }

inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

const int M = 10;
const int N = 30 + 3;

int n, m, maxd;
char f[N][N];
vector<pti> ss, ts;

bool read() {
    if (scanf("%d%d%d", &m, &n, &maxd) != 3) return false;
    forn(i, n) assert(scanf("%s", f[i]) == 1);
    return true;
}

int canShoot[(1 << M) + 3][M + 3];

int used[N][N];
int z[N][N];
vector<int> dx{-1, 1, 0, 0};
vector<int> dy{0, 0, 1, -1};

void calcShoot(int maskT, int s) {
    memset(used, 0, sizeof(used));
    forn(i, sz(ts)) {
        if ((maskT & (1 << i)) == 0) continue;
        int tx = ts[i].x, ty = ts[i].y;
        used[tx][ty] |= (1 << i);
        forn(dir, sz(dx)) {
            int len = 1;
            while (true) {
                int nx = tx + dx[dir] * len, ny = ty + dy[dir] * len;
                if (!correct(nx, ny, n, m) || f[nx][ny] == '#') break;
                used[nx][ny] |= (1 << i);
                len++;
            }
        }
    }

    forn(i, n) forn(j, m) z[i][j] = INF;
    z[ss[s].x][ss[s].y] = 0;
    canShoot[maskT][s] |= used[ss[s].x][ss[s].y];
    queue<pti> q;
    q.push(ss[s]);
    while (!q.empty()) {
        int x = q.front().x, y = q.front().y;
        q.pop();
        canShoot[maskT][s] |= used[x][y];
        if (used[x][y] != 0 || z[x][y] >= maxd) continue;
        forn(dir, sz(dx)) {
            int nx = x + dx[dir], ny = y + dy[dir];
            if (!correct(nx, ny, n, m) || f[nx][ny] == '#') continue;
            if (z[nx][ny] > z[x][y] + 1) {
                z[nx][ny] = z[x][y] + 1;
                q.push(mp(nx, ny));
            }
        }
    }
}

int d[(1 << M) + 3][(1 << M) + 3];
vector<pti> ansvec;

int calc(int maskT, int maskS) {
    int& ans = d[maskT][maskS];
    if (ans != -1) return ans;
    ans = 0;

    forn(i, sz(ss)) {
        if ((maskS & (1 << i)) == 0) continue;
        forn(j, sz(ts)) {
            if ((maskT & (1 << j)) && (canShoot[maskT][i] & (1 << j))) {
                int val = calc(maskT ^ (1 << j), maskS ^ (1 << i)) + 1;
                ans = max(ans, val);
            }
        }
    }
    return ans;
}

void restore(int maskT, int maskS) {
    const int& ans = d[maskT][maskS];

    forn(i, sz(ss)) {
        if ((maskS & (1 << i)) == 0) continue;
        forn(j, sz(ts)) {
            if ((maskT & (1 << j)) && (canShoot[maskT][i] & (1 << j))) {
                int val = calc(maskT ^ (1 << j), maskS ^ (1 << i)) + 1;
                if (val == ans) {
                    ansvec.pb(mp(i, j));
                    restore(maskT ^ (1 << j), maskS ^ (1 << i));
                    return;
                }
            }
        }
    }
}

void solve() {
    ss.clear();
    ts.clear();
    forn(i, n) forn(j, m) {
        if (f[i][j] == 'S') ss.pb(mp(i, j));
        if (f[i][j] == 'T') ts.pb(mp(i, j));
    }

    memset(canShoot, 0, sizeof(canShoot));
    forn(maskT, (1 << sz(ts))) {
        forn(i, sz(ss)) {
            calcShoot(maskT, i);
        }
    }

    memset(d, -1, sizeof(d));
    const int startTmask = (1 << sz(ts)) - 1, startSmask = (1 << sz(ss)) - 1;
    int ans = calc(startTmask, startSmask);
    ansvec.clear();
    restore(startTmask, startSmask);
    printf("%d\n", ans);
    forn(i, sz(ansvec)) printf("%d %d\n", ansvec[i].x + 1, ansvec[i].y + 1);
}

int main() {
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;

    int testCount;
    assert(scanf("%d", &testCount) == 1);
    forl(test, testCount) {
        ld stime = gett();
        printf("Case #%d: ", test);
        read();
        solve();
        cerr << "Test = " << test << "; time: " << gett() - stime << endl;
        //break;
    }
    
    return 0;
}

