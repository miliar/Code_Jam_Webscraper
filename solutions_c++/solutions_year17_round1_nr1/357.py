#include <bits/stdc++.h>
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
using namespace std;
typedef long long ll;
#define mp make_pair
#define fi first
#define se second
#define pb push_back

const double pi = acos(-1.0);
const int inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3fll;
const int MAX_N = 10010;

int T, R, C, cases = 0;
char str[30][30], ans[30][30];

void solve() {
    /*
    int vis[30][30];
    memset(vis, 0, sizeof (vis));
    for (int i = 1; i <= R; ++i) {
        int full = 1;
        for (int j = 1; j <= C; ++j) {
            if (str[i][j] != '?') {
                full = 0;
                break;
            }
        }

        if (full) {
            for (int j = 1; j <= C; ++j) {
                int find = 0;
                for (int k = i - 1; k >= 1; --k) {
                    if (ans[k][j] != '?') {
                        find = k;
                        for (int p = k - 1; p <= i; ++p) {
                            ans[p][j] = ans[k][j];
                        }
                        vis[k][j] = 1;
                        break;
                    }
                }

                if (!find) {
                    for (int k = i + 1; k <= R; ++k) {
                        if (ans[k][j] != '?') {
                            find = k;
                            for (int p = i; p <= k; ++p) {
                                ans[p][j] = ans[k][j];
                            }
                            vis[k][j] = 1;
                            break;
                        }
                    }
                }

                assert(find != 0);
            }
        }
    }
*/
    for (int i = 1; i <= R; ++i) {
        for (int j = 1; j <= C; ++j) {
            if (ans[i][j] != '?') {
                for (int p = j - 1; p >= 1; --p) {
                    if (ans[i][p] != '?') break;
                    ans[i][p] = ans[i][j];
                }

                for (int p = j + 1; p <= C; ++p) {
                    if (ans[i][p] != '?') break;
                    ans[i][p] = ans[i][j];
                }
            }
        }
    }

    for (int i = 1; i <= R; ++i) {
        if (ans[i][1] == '?') {
            int find = 0;
            for (int j = i - 1; j >= 1; --j) {
                if (ans[j][1] != '?') {
                    for (int k = 1; k <= C; ++k) {
                        ans[i][k] = ans[j][k];
                    }
                    find = 1;
                    break;
                }
            }

            if (find) continue;

            for (int j = i + 1; j <= R; ++j) {
                if (ans[j][1] != '?') {
                    for (int k = 1; k <= C; ++k) {
                        ans[i][k] = ans[j][k];
                    }
                    find = 1;
                    break;
                }
            }

            assert(find != 0);
        }
    }
}

int main() {    
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);

    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &R, &C);
        for (int i = 1; i <= R; ++i) {
            scanf("%s", str[i] + 1);
            for (int j = 1; j <= C + 1; ++j) {
                ans[i][j] = str[i][j];
            }
        }
        solve();
        printf("Case #%d:\n", ++cases);
        for (int i = 1; i <= R; ++i) {
            printf("%s\n", ans[i] + 1);
        }
    }
    return 0;
}
    
