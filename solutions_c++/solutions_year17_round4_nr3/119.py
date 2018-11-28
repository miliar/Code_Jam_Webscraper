#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long LL;
typedef pair<int, int> PII;

int test, tt;
int r, c;
char s[50][55];
//R D L U
const int dy[4] = {0, 1, 0, -1};
const int dx[4] = {1, 0, -1, 0};
bool used[50][50][4];
int can[2500][2];
vector<int> gg[2500];
vector<int> g[5000], inv[5000];

bool check(int y, int x, int dir) {
    while (true) {
        if (y < 0 || y >= r || x < 0 || x >= c) {
            return true;
        }
        if (used[y][x][dir]) {
            return true;
        }
        if (s[y][x] == '#') {
            return true;
        }
        if (s[y][x] == '|' || s[y][x] == '-') {
            return false;
        }
        used[y][x][dir] = true;
        if (s[y][x] == '\\') {
            if (dir == 0) dir = 1;
            else if (dir == 1) dir = 0;
            else if (dir == 2) dir = 3;
            else dir = 2;
        }
        if (s[y][x] == '/') {
            if (dir == 0) dir = 3;
            else if (dir == 3) dir = 0;
            else if (dir == 1) dir = 2;
            else dir = 1;
        }
        y += dy[dir];
        x += dx[dir];
    }
    return true;
}

bool u[5000];
vector<int> ord;
int cmp[5000];

void dfs1(int v) {
    u[v] = true;
    for (int to : g[v]) if (!u[to]) {
        dfs1(to);
    }
    ord.pb(v);
}

void dfs2(int v, int c) {
    cmp[v] = c;
    for (int to : inv[v]) if (cmp[to] == -1) {
        dfs2(to, c);
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tt);
    for (test = 1; test <= tt; ++test) {
        memset(can, 0, sizeof can);
        printf("Case #%d: ", test);
        scanf("%d%d", &r, &c);
        forn(i, r) scanf("%s", s[i]);
        bool ok = true;
        forn(i, r * c) gg[i].clear();
        forn(i, r) if (ok) forn(j, c) if (s[i][j] == '|' || s[i][j] == '-') {
            memset(used, 0, sizeof used);
            int num = i * c + j;
            if (check(i, j + 1, 0) && check(i, j - 1, 2)) {
                can[num][0] = true;
                forn(ii, r) forn(jj, c) if (s[ii][jj] == '.') forn(dir, 4) {
                    if (used[ii][jj][dir]) {
                        gg[ii * c + jj].pb(2 * num);
                        break;
                    }
                }
            }
            memset(used, 0, sizeof used);
            if (check(i + 1, j, 1) && check(i - 1, j, 3)) {
                can[num][1] = true;
                forn(ii, r) forn(jj, c) if (s[ii][jj] == '.') forn(dir, 4) {
                    if (used[ii][jj][dir]) {
                        gg[ii * c + jj].pb(2 * num + 1);
                        break;
                    }
                }
            }
            if (!can[num][0] && !can[num][1]) {
                ok = false;
                break;
            }
        }
        if (!ok) {
            printf("IMPOSSIBLE\n");
            cerr << "Done " << test << endl;
            continue;
        }
        forn(i, 2 * r * c) g[i].clear();
        forn(i, r) if (ok) forn(j, c) if (s[i][j] == '.') {
            if (gg[i * c + j].empty()) {
                ok = false;
                break;
            }
        }
        if (!ok) {
            printf("IMPOSSIBLE\n");
            cerr << "Done " << test << endl;
            continue;
        }
        forn(i, 2 * r * c) g[i].clear();
        forn(i, r) forn(j, c) if (s[i][j] == '.') {
            int num = i * c + j;
            assert((int)gg[num].size() <= 2);
            if ((int)gg[num].size() == 1) {
                g[gg[num][0] ^ 1].pb(gg[num][0]);
            } else {
                int x = gg[num][0];
                int y = gg[num][1];
                if ((x ^ y) != 1) {
                    g[x ^ 1].pb(y);
                    g[y ^ 1].pb(x);
                }
            }
        }
        forn(i, r) forn(j, c) if (s[i][j] == '-' || s[i][j] == '|') {
            int num = i * c + j;
            if (!can[num][0]) {
                g[2 * num].pb(2 * num + 1);
            }
            if (!can[num][1]) {
                g[2 * num + 1].pb(2 * num);
            }
        }
        int cnt = 2 * r * c;
        forn(i, cnt) inv[i].clear();
        forn(i, cnt) for (int to : g[i]) {
            inv[to].pb(i);
        }
        memset(u, 0, sizeof u);
        forn(i, cnt) if (!u[i]) {
            dfs1(i);
        }
        memset(cmp, -1, sizeof cmp);
        reverse(ord.begin(), ord.end());
        int cnum = 0;
        forn(ii, cnt) {
            int i = ord[ii];
            if (cmp[i] == -1) {
                dfs2(i, cnum);
                ++cnum;
            }
        }
        for (int i = 0; i < cnt; i += 2) {
            if (cmp[i] == cmp[i ^ 1]) {
                ok = false;
                break;
            }
        }
        if (!ok) {
            printf("IMPOSSIBLE\n");
            cerr << "Done " << test << endl;
            continue;
        }
        for (int i = 0; i < cnt; i += 2) {
            int num = i / 2;
            int row = num / c;
            int col = num % c;
            if (s[row][col] != '-' && s[row][col] != '|') {
                continue;
            }
            if (cmp[i] < cmp[i ^ 1]) {
                s[row][col] = '|';
            } else {
                s[row][col] = '-';
            }
        }
        printf("POSSIBLE\n");
        forn(i, r) printf("%s\n", s[i]);

        cerr << "Done " << test << endl;
    }
    return 0;
}
