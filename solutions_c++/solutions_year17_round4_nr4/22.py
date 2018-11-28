#include <bits/stdc++.h>
using namespace std;
#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
#define all(x) (x).begin(), (x).end()
typedef long long ll;
typedef long long i64;
typedef long double ld;
const int inf = int(1e9) + int(1e5);
const ll infl = ll(2e18) + ll(1e10);
typedef pair<int, int> pii;

const int maxn = 105;
const int maxk = 10;
int n, m, r;
string s[maxn];
bool d[1 << maxk][1 << maxk];
int from1[1 << maxk][1 << maxk];
int from2[1 << maxk][1 << maxk];
vector<pii> S;
vector<pii> T;
int sc, tc;

const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, -1, 0, 1};

vector<int> who[maxn][maxn];
bool avail[maxk][maxk];

int dist[maxn][maxn];
vector<pii> q;
void bfs(int id) {
    int sx, sy;
    tie(sx, sy) = S[id];
    forn (i, n)
        forn (j, m)
            dist[i][j] = inf;
    dist[sx][sy] = 0;
    q.clear();
    q.emplace_back(sx, sy);
    forn (ii, sz(q)) {
        int x, y;
        tie(x, y) = q[ii];
        if (!who[x][y].empty()) {
            for (auto to: who[x][y])
                avail[id][to] = true;
            continue;
        }
        if (dist[x][y] >= r)
            continue;
        forn (dir, 4) {
            int tx = x + dx[dir];
            int ty = y + dy[dir];
            if (tx < 0 || tx >= n || ty < 0 || ty >= m || s[tx][ty] == '#')
                continue;
            if (dist[tx][ty] != inf)
                continue;
            dist[tx][ty] = dist[x][y] + 1;
            q.emplace_back(tx, ty);
        }
    }
}

int test = 1;
void solve() {
    cin >> m >> n >> r;
    forn (i, n)
        cin >> s[i];
    S.clear();
    T.clear();
    forn (i, n)
        forn (j, m) {
            if (s[i][j] == 'T')
                T.emplace_back(i, j);
            if (s[i][j] == 'S')
                S.emplace_back(i, j);
        }
    sc = sz(S);
    tc = sz(T);
    forn (i, 1 << tc)
        forn (j, 1 << sc)
            d[i][j] = false;
    d[0][0] = true;
    int res = 0;
    int rm1 = 0, rm2 = 0;
    forn (tm, 1 << tc) {
        forn (i, n)
            forn (j, m)
                who[i][j].clear();
        forn (t, tc) {
            if (tm & (1 << t))
                continue;
            int x, y;
            tie(x, y) = T[t];
            who[x][y].push_back(t);
            forn (dir, 4) {
                tie(x, y) = T[t];
                while (true) {
                    x += dx[dir];
                    y += dy[dir];
                    if (x < 0 || x >= n || y < 0 || y >= m || s[x][y] == '#')
                        break;
                    who[x][y].push_back(t);
                }
            }
        }
        forn (i, sc) {
            forn (j, tc)
                avail[i][j] = false;
            bfs(i);
        }
        forn (sm, 1 << sc) {
            if (!d[tm][sm])
                continue;
            forn (s, sc) {
                if (sm & (1 << s))
                    continue;
                forn (t, tc) {
                    if (tm & (1 << t))
                        continue;
                    if (!avail[s][t])
                        continue;
                    int ntm = tm | (1 << t);
                    int nsm = sm | (1 << s);
                    d[ntm][nsm] = true;
                    from1[ntm][nsm] = t;
                    from2[ntm][nsm] = s;
                    int cur = __builtin_popcount(ntm);
                    if (cur > res) {
                        res = cur;
                        rm1 = ntm;
                        rm2 = nsm;
                    }
                }
            }
        }
    }
    vector<pii> op;
    while (rm1 > 0) {
        int b1 = from1[rm1][rm2];
        int b2 = from2[rm1][rm2];
        op.emplace_back(b2, b1);
        rm1 ^= 1 << b1;
        rm2 ^= 1 << b2;
    }
    reverse(all(op));
    cout << "Case #" << test++ << ": " << res << '\n';
    for (auto p: op)
        cout << p.first + 1 << ' ' << p.second + 1 << '\n';
}

int main() {
    #ifdef LOCAL
    assert(freopen("d.in", "r", stdin));
    #else
    #endif
    int tn;
    cin >> tn;
    forn (i, tn)
        solve();
}
