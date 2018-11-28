#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define first fi
#define second se
#define sz(x) (int)x.size()
#define mp(a,b) make_pair(a,b)
#define pb push_back
const int inf = 0x3f3f3f3f;
const int mod = 1e9+7;

const int N = 105;
int T, n, p, g[N];
int cnt[10];
int dp[N][N][N];

int dfs(int a, int b, int c) {
    if (dp[a][b][c] != -1) return dp[a][b][c];
    if (a == 0 && b == 0 && c == 0) return dp[a][b][c] = 0;
    dp[a][b][c] = 1;
    for (int i = 0; i <= 4 && i <= a; i++) {
        for (int j = 0; j <= 4 && j <= b; j++) {
            for (int k = 0; k <= 4 && k <= c; k++) {
                if (i == 0 && j == 0 && k == 0) continue;
                if ((i + 2 * j + 3 * k) % 4 == 0) {
                    dp[a][b][c] = max(dp[a][b][c], dfs(a - i, b - j, c - k) + 1);
                }
            }
        }
    }
  //  printf("%d %d %d %d\n", a, b, c, dp[a][b][c]);
    return dp[a][b][c];
}

int main() {
    freopen("A-large (2).in", "r", stdin);
    freopen("A-large (2).out", "w", stdout);
    int cas = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &n, &p);
        memset(cnt, 0, sizeof(cnt));
        for (int i = 1; i <= n; i++) {
            int x; scanf("%d", &x);
            cnt[x % p]++;
        }
        printf("Case #%d: ", ++cas);
        if (p == 2) {
            printf("%d\n", cnt[0] + (cnt[1] + 1) / 2);
        } else if (p == 3) {
            int use = min(cnt[1], cnt[2]);
            cnt[1] -= use; cnt[2] -= use;
            printf("%d\n", cnt[0] + use + (cnt[1] + 2) / 3 + (cnt[2] + 2 ) / 3);
        } else {
            memset(dp, -1, sizeof(dp));
            printf("%d\n", cnt[0] + dfs(cnt[1], cnt[2], cnt[3]));
        }
    }
    return 0;
}
