#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define ft first
#define sd second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()

#ifdef LOCAL
#define eprint(x) cerr << #x << " = " << x << endl
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprint(x)
#define eprintf(...)
#endif

typedef long long ll;
typedef pair<int, int> pii;
typedef long double ld;

const int INF = 1e9;
const int N = 100;
const int P = 4;

int g[N], cnt[P], dp[N + 1][N + 1][N + 1][P];

int main() {
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  int tt;
  cin >> tt;
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    int n, p;
    cin >> n >> p;
    for (int i = 0; i < P; i++)
      cnt[i] = 0;
    for (int i = 0; i < n; i++) {
      cin >> g[i];
      cnt[g[i] % p]++;
    }
    for (int i = 0; i <= N; i++)
      for (int j = 0; j <= N; j++)
        for (int k = 0; k <= N; k++)
          for (int r = 0; r < P; r++)
            dp[i][j][k][r] = -INF;
    dp[0][0][0][0] = 0;
    for (int i = 0; i <= cnt[1]; i++)
      for (int j = 0; j <= cnt[2]; j++)
        for (int k = 0; k <= cnt[3]; k++)
          for (int r = 0; r < p; r++) {
            if (dp[i][j][k][r] == -INF)
              continue;
            if (i < cnt[1]) {
              int nr = (r + 1) % p;
              dp[i + 1][j][k][nr] = max(dp[i][j][k][r] + (r == 0), dp[i + 1][j][k][nr]);
            }
            if (j < cnt[2]) {
              int nr = (r + 2) % p;
              dp[i][j + 1][k][nr] = max(dp[i][j][k][r] + (r == 0), dp[i][j + 1][k][nr]);
            }
            if (k < cnt[3]) {
              int nr = (r + 3) % p;
              dp[i][j][k + 1][nr] = max(dp[i][j][k][r] + (r == 0), dp[i][j][k + 1][nr]);
            }
          }
    int ans = 0;
    for (int r = 0; r < p; r++)
      ans = max(dp[cnt[1]][cnt[2]][cnt[3]][r], ans);
    printf("%d\n", ans + cnt[0]);
  }
#ifdef LOCAL
  eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  return 0;
}