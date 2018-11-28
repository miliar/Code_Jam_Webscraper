#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <functional>
#include <map>
#include <bitset>

#define INF 0x7fffffff
#define REP(i,j,k) for(int i = j;i <= k;i++)
#define squr(x) (x) * (x)
#define lowbit(x) (x&(-x))
#define getint(x) scanf("%d", &(x))

typedef long long LL;

using namespace std;

int n, m;
int T;
int f[110][110];
int ff[110][110];
int f1[110][110], f2[110][110];
char s[20];
char c;
int x, y;
bool visx[110], visy[110];
bool visxx[210], visyy[210];
bool vis[210];
int match[210];

vector<int>edge[210];

void addedge(int e1, int e2) {
    edge[e1].push_back(e2);
    //edge[e2].push_back(e1);
}

bool dfs(int node) {
    int sz = (int)edge[node].size();
    for (int i = 0; i < sz; i++) {
        int go = edge[node][i];
        if (!vis[go]) {
            vis[go] = true;
            if (!match[go] || dfs(match[go])) {
                match[go] = node;
                return true;
            }
        }
        
    }
    return false;
}

int main(int argc, const char * argv[]) {
    //freopen("D-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    cin >> T;
    REP(ca, 1, T) {
        cin >> n >> m;
        int ans = 0, count = 0;
        
        memset(f, 0, sizeof(f));
        memset(ff, 0, sizeof(ff));
        memset(f1, 0, sizeof(f1));
        memset(f2, 0, sizeof(f2));
        memset(visx, 0, sizeof(visx));
        memset(visy, 0, sizeof(visy));
        memset(visxx, 0, sizeof(visxx));
        memset(visyy, 0, sizeof(visyy));
        //memset(vis, 0, sizeof(vis));
        memset(match, 0, sizeof(match));
        REP(i, 0, 209) {
            edge[i].clear();
        }
        
        REP(i, 1, m) {
            scanf("%s%d%d", s, &x, &y);
            c = s[0];
            if (c == '+') {
                f[x][y] = 2;
                f2[x][y] = 2;
                visxx[x + y] = true;
                visyy[x - y + n] = true;
            } else if (c == 'x') {
                f[x][y] = 1;
                f1[x][y] = 1;
                visx[x] = true;
                visy[y] = true;
            } else {
                f[x][y] = 3;
                f1[x][y] = 1;
                f2[x][y] = 2;
                visx[x] = true;
                visy[y] = true;
                visxx[x + y] = true;
                visyy[x - y + n] = true;
            }
        }
        
        int ti = 1, tj = 1;
        while (ti <= n && tj <= n) {
            while (visx[ti] && ti <= n) {
                ti++;
            }
            while (visy[tj] && tj <= n) {
                tj++;
            }
            f1[ti][tj] = 1;
            visx[ti] = true;
            visy[tj] = true;
        }
        
        for (int i = 2; i <= 2 * n; i++) {
            if (visxx[i]) {
                continue;
            }
            for (int j = max(1, i - n); j < i && j <= n; j++) {
                if (!visyy[2 * j - i + n]) {
                    addedge(i, 2 * j - i + n);
                }
            }
        }
        
        REP(i, 2, 2 * n) {
            memset(vis, 0, sizeof(vis));
            dfs(i);
        }
        
        REP(i, 1, 2 * n - 1) {
            if (match[i]) {
                x = (i + match[i] - n) / 2;
                y = match[i] - x;
                f2[x][y] = 2;
            }
            
        }
        REP(i, 1, n) {
            REP(j, 1, n) {
                if (f1[i][j]) {
                    ff[i][j] = 1;
                }
                if (f2[i][j]) {
                    ff[i][j] += 2;
                }
                if (ff[i][j] != f[i][j]) {
                    ans++;
                }
                if (ff[i][j] > 0 && ff[i][j] < 3) {
                    count++;
                } else if (ff[i][j] == 3) {
                    count += 2;
                }
            }
        }
        printf("Case #%d: %d %d\n", ca, count, ans);
        REP(i, 1, n) {
            REP(j, 1, n) {
                if (ff[i][j] != f[i][j]) {
                    if (ff[i][j] == 1) {
                        printf("x %d %d\n", i, j);
                    } else if (ff[i][j] == 2) {
                        printf("+ %d %d\n", i, j);
                    } else {
                        printf("o %d %d\n", i, j);
                    }
                }
            }
        }
    }
    return 0;
}









