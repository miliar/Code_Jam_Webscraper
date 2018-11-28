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
typedef unsigned long long ull;
typedef long double ld;

const int INF = 1e9;
const int T = 1440;
const int D = 720;

int dp[T + 1][T + 1][2][2];
bool a[T + 1], b[T + 1];

int main() {
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  int tt;
  cin >> tt;
  for (int qq = 1; qq <= tt; qq++) {
    for (int i = 0; i <= T; i++) {
      a[i] = b[i] = 0;
      for (int j = 0; j <= T; j++) {
        dp[i][j][0][0] = dp[i][j][1][0] = INF;
        dp[i][j][0][1] = dp[i][j][1][1] = INF;
      }
    }
    printf("Case #%d: ", qq);
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
      int l, r;
      cin >> l >> r;
      for (int j = l; j < r; j++)
        a[j] = 1;
    }
    for (int i = 0; i < m; i++) {
      int l, r;
      cin >> l >> r;
      for (int j = l; j < r; j++)
        b[j] = 1;
    }
    dp[0][D][0][0] = dp[0][D][1][1] = 0;
    for (int i = 0; i < T; i++)
      for (int d = 0; d <= T; d++)
        for (int j = 0; j < 2; j++)
          for (int k = 0; k < 2; k++) {
            if (dp[i][d][j][k] == INF)
              continue;
            if (!a[i] && d + 1 <= T)
              dp[i + 1][d + 1][0][k] = min(dp[i + 1][d + 1][0][k], dp[i][d][j][k] + (j == 1));
            if (!b[i] && d - 1 >= 0)
              dp[i + 1][d - 1][1][k] = min(dp[i + 1][d - 1][1][k], dp[i][d][j][k] + (j == 0));
          }
    cout << min(min(dp[T][D][0][0], dp[T][D][1][1]), min(dp[T][D][0][1] + 1, dp[T][D][1][0] + 1)) << endl;
  }
#ifdef LOCAL
  eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  return 0;
}