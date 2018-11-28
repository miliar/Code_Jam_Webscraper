#include <map>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int T, n, k, score;
int g1[256][256];
int m1[256];
bool v1[256];
int g2[256][256];
int m2[256];
bool v2[256];
bool oh[256], ol[256], om[256], os[256];
int op[256][256], ox[256][256];
int ap[256][256], ax[256][256];
int np;
char pc[26384];
int px[16384], py[16384];

bool match(int g[][256], int m[], bool vis[], int n, int u) {
    for (int v = 0; v < n; ++v) 
        if (g[u][v] && !vis[v]) {
            vis[v] = true;
            if (m[v] == -1 || match(g, m, vis, n, m[v])) {
                m[v] = u;
                return true;
            }
        }
    return false;
}

int main() {
    scanf("%d\n", &T);
    for (int test = 1; test <= T; ++test) {
        memset(g1, 0, sizeof(g1));
        memset(g2, 0, sizeof(g2));
        memset(m1, -1, sizeof(m1));
        memset(m2, -1, sizeof(m2));
        memset(oh, 0, sizeof(oh));
        memset(ol, 0, sizeof(ol));
        memset(om, 0, sizeof(om));
        memset(os, 0, sizeof(os));
        memset(op, 0, sizeof(op));
        memset(ox, 0, sizeof(ox));
        memset(ap, 0, sizeof(ap));
        memset(ax, 0, sizeof(ax));
        scanf("%d %d\n", &n, &k);
        score = 0;
        for (int i = 0; i < k; ++i) {
            char c[8];
            int x, y;
            scanf("%s %d %d\n", c, &x, &y);
            x--;
            y--;
            if (c[0] == 'x' || c[0] == 'o') {
                score ++;
                oh[x] = true;
                ol[y] = true;
                op[x][y] = 1;
            }
            if (c[0] == '+' || c[0] == 'o') {
                score ++;
                om[x - y + n - 1] = true;
                os[x + y] = true;
                ox[x][y] = 1;
            }
        }
        for (int x = 0; x < n; ++x)
            for (int y = 0; y < n; ++y) {
                if (!oh[x] && !ol[y])
                    g1[x][y] = 1;
                if (!om[x - y + n - 1] && !os[x + y])
                    g2[x - y + n - 1][x + y] = 1;
            }
        for (int i = 0; i < n; ++i) {
            memset(v1, 0, sizeof(v1));
            if (match(g1, m1, v1, n, i))
                score ++;
        }
        for (int i = 0; i < n * 2 - 1; ++i) {
            memset(v2, 0, sizeof(v2));
            if (match(g2, m2, v2, n * 2 - 1, i))
                score ++;
        }
        for (int i = 0; i < n; ++i)
            if (m1[i] != -1) {
                int x = m1[i];
                int y = i;
                ap[x][y] = 1;
            }
        for (int i = 0; i < n * 2 - 1; ++i)
            if (m2[i] != -1) {
                int s = i, d = m2[i] - (n - 1);
                int x = (s + d) / 2, y = (s - d) / 2;
                ax[x][y] = 1;
            }
        np = 0;
        for (int x = 0; x < n; ++x)
            for (int y = 0; y < n; ++y)
                if (ap[x][y] + ax[x][y] > 0) {
                    if (ap[x][y] + ax[x][y] + op[x][y] + ox[x][y] == 2) {
                        pc[np] = 'o';
                        px[np] = x + 1;
                        py[np] = y + 1;
                        np ++;
                    } else if (ap[x][y] > 0) {
                        pc[np] = 'x';
                        px[np] = x + 1;
                        py[np] = y + 1;
                        np ++;
                    } else if (ax[x][y] > 0) {
                        pc[np] = '+';
                        px[np] = x + 1;
                        py[np] = y + 1;
                        np ++;
                    }
                }
        printf("Case #%d: %d %d\n", test, score, np);
        for (int i = 0; i < np; ++i)
            printf("%c %d %d\n", pc[i], px[i], py[i]);
    }
    return 0;
}