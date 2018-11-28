#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define first fi
#define second se
#define sz(x) (int)x.size()
#define mp(a,b) make_pair(a,b)
const int inf = 0x3f3f3f3f;
const int mod = 1e9+7;

const int N = 30;
int T, n, m;
char g[N][N];
int vis[N];

bool judge(int v, int l, int r) {
    for (int i = l; i <= r; i++) if (g[v][i] != '?') return false;
    return true;
}

int main() {
    freopen("A-large (1).in", "r", stdin);
    freopen("A-large (1).out", "w", stdout);
    int cas = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; i++)scanf("%s", g[i] + 1);
        memset(vis, 0, sizeof(vis));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (g[i][j] != '?' && !vis[g[i][j] - 'A']) {
                    vis[g[i][j] - 'A'] = 1;
                    char tmp = g[i][j];
                    g[i][j] = '?';
                    int l = j, r = j;
                    while (l > 0 && judge(i, l, r)) l--; l++;
                    while (r <= m && judge(i, l, r)) r++; r--;
                    int u = i, d = i;
                    while (u > 0 && judge(u, l, r)) u--; u++;
                    while (d <= n && judge(d, l, r)) d++; d--;
                  //  printf("%d %d %d %d %d %d\n", i, j, u, l, d, r);
                    for (int x = u; x <=d ;x++)
                        for (int y = l; y<=r; y++)
                            g[x][y] = tmp;
                }
            }
        }
        printf("Case #%d:\n", ++cas);
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                printf("%c", g[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
