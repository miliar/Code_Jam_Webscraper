/******************************************************************************\
*                         Author:  Dumbear                                     *
*                         Email:   dumbear[#at]163.com                         *
*                         Website: http://dumbear.com                          *
\******************************************************************************/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>

using namespace std;

#define output(x) cout << #x << ": " << (x) << endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<long long> VL;
typedef vector<double> VD;
typedef vector<string> VS;

int t, n, m;
char grid[64][64];
int step[][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
bool vis[64][64][4];
bool cmask[64][64], mask[64][64];
vector<pair<int, int> > shooters, cell;
int cnt[3000];
bool ok;
vector<int> g[3000][2];
int way[3000];
vector<pair<int, int> > ways[3000];

bool shooter(int i, int j) {
    char c = grid[i][j];
    return c == '|' || c == '-';
}

bool mirror(int i, int j) {
    char c = grid[i][j];
    return c == '/' || c == '\\';
}

void dfs(int x, int y, int dir) {
    cmask[x][y] = true;
    if (vis[x][y][dir])
        return;
    vis[x][y][dir] = true;
    int nx = x + step[dir][0];
    int ny = y + step[dir][1];
    if (nx >= 0 && nx < n && ny >= 0 && ny < m && grid[nx][ny] != '#') {
        int ndir = dir;
        if (shooter(nx, ny)) {
            ok = false;
        }
        if (grid[nx][ny] == '/') {
            ndir = (dir < 2 ? 1 - dir : 5 - dir);
        } else if (grid[nx][ny] == '\\') {
            ndir = 3 - dir;
        }
        dfs(nx, ny, ndir);
    }
}

bool check(int x, int y) {
    memset(vis, 0, sizeof(vis));
    memset(cmask, 0, sizeof(cmask));
    ok = true;
    dfs(x, y, grid[x][y] == '-' ? 1 : 0);
    dfs(x, y, grid[x][y] == '-' ? 3 : 2);
    return ok;
}

bool dfs2(int k) {
    if (k == shooters.size()) {
        bool all = true;
        for (int i = 0; i < cell.size(); ++i) {
            if (cnt[i] == 0) {
                all = false;
                break;
            }
        }
        return all;
    }
    int a = shooters[k].first;
    int b = shooters[k].second;
    grid[a][b] = '-';
    for (int i = 0; i < g[k][0].size(); ++i) {
        ++cnt[g[k][0][i]];
    }
    if (dfs2(k + 1)) return true;
    for (int i = 0; i < g[k][0].size(); ++i) {
        --cnt[g[k][0][i]];
    }
    grid[a][b] = '|';
    for (int i = 0; i < g[k][1].size(); ++i) {
        ++cnt[g[k][1][i]];
    }
    if (dfs2(k + 1)) return true;
    for (int i = 0; i < g[k][1].size(); ++i) {
        --cnt[g[k][1][i]];
    }
    return false;
}

bool preprocess() {
    shooters.clear();
    memset(mask, 0, sizeof(mask));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (shooter(i, j)) {
                grid[i][j] = '-';
                bool c1 = check(i, j);
                grid[i][j] = '|';
                bool c2 = check(i, j);
                if (!c1 && !c2)
                    return false;
                if (c1 && c2) {
                    shooters.push_back(make_pair(i, j));
                } else if (c1) {
                    grid[i][j] = '-';
                    check(i, j);
                    for (int x = 0; x < n; ++x) {
                        for (int y = 0; y < m; ++y) {
                            mask[x][y] |= cmask[x][y];
                        }
                    }
                } else if (c2) {
                    grid[i][j] = '|';
                    check(i, j);
                    for (int x = 0; x < n; ++x) {
                        for (int y = 0; y < m; ++y) {
                            mask[x][y] |= cmask[x][y];
                        }
                    }
                }
            }
        }
    }
    cell.clear();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '.' && !mask[i][j]) {
                cell.push_back(make_pair(i, j));
                // printf("-- cell: %d %d\n", i, j);
            }
        }
    }
    // printf("cell size: %d\n", (int)cell.size());
    // printf("shooters size: %d\n", (int)shooters.size());
    for (int i = 0; i < cell.size(); ++i) {
        ways[i].clear();
    }
    for (int i = 0; i < shooters.size(); ++i) {
        // output(i);
        way[i] = -1;
        g[i][0].clear();
        g[i][1].clear();
        int a = shooters[i].first;
        int b = shooters[i].second;
        // printf("-- shooter: %d %d\n", a, b);
        grid[a][b] = '-';
        check(a, b);
        for (int j = 0; j < cell.size(); ++j) {
            int x = cell[j].first;
            int y = cell[j].second;
            if (cmask[x][y]) {
                ways[j].push_back(make_pair(i, 0));
                g[i][0].push_back(j);
            }
        }
        grid[a][b] = '|';
        check(a, b);
        for (int j = 0; j < cell.size(); ++j) {
            int x = cell[j].first;
            int y = cell[j].second;
            if (cmask[x][y]) {
                ways[j].push_back(make_pair(i, 1));
                g[i][1].push_back(j);
            }
        }
    }
    for (int i = 0; i < cell.size(); ++i) {
        if (ways[i].size() == 0) return false;
        if (ways[i].size() == 1) {
            if (way[ways[i][0].first] != -1 && way[ways[i][0].first] != ways[i][0].second)
                return false;
            way[ways[i][0].first] = ways[i][0].second;
        }
    }
    return true;
}

void solve() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i)
        scanf("%s", grid[i]);
    if (!preprocess()) {
        printf("Case #%d: IMPOSSIBLE\n", ++t);
    } else {
        memset(cnt, 0, sizeof(cnt));
        // puts("!!!!!!");
        if (dfs2(0)) {
            printf("Case #%d: POSSIBLE\n", ++t);
            for (int i = 0; i < n; ++i)
                puts(grid[i]);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", ++t);
        }
    }
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
