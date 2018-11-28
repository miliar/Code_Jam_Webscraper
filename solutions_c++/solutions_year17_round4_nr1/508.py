#include <bits/stdc++.h>

using namespace std;

#define INF 100000000
#define YJ 1145141919
#define INF_INT_MAX 2147483647
#define INF_LL_MAX 9223372036854775807
#define EPS 1e-10
#define Pi acos(-1)
#define LL long long
#define ULL unsigned long long
#define LD long double

using namespace std;

#define MAX_N 105

#define MAX_P 4

int T;
int N, P;
int G[MAX_N];

int K[MAX_P];

void init()
{
  memset(G, 0, sizeof(G));
  memset(K, 0, sizeof(K));
}

int dp[MAX_N][MAX_N][MAX_N][4];

int main()
{
  cin >> T;
  for (int testCase = 1; testCase <= T; testCase++) {
    init();
    cin >> N >> P;
    for (int i = 0; i < N; i++) {
      cin >> G[i];
    }

    for (int i = 0; i < N; i++) {
      K[G[i] % P]++;
    }

    int ans = K[0];

    for (int i = 0; i < MAX_N; i++) {
      for (int j = 0; j < MAX_N; j++) {
        for (int k = 0; k < MAX_N; k++) {
          for (int d = 0; d < 4; d++) {
            dp[i][j][k][d] = -INF;
          }
        }
      }
    }

    dp[0][0][0][0] = 0;

    for (int i = 0; i <= K[1]; i++) {
      for (int j = 0; j <= K[2]; j++) {
        for (int k = 0; k <= K[3]; k++) {
          for (int d = 0; d < 4; d++) {

            if(dp[i][j][k][d] == -INF){
              continue;
            }

            int bonus = (d == 0 ? 1 : 0);

            if(i+1 <= K[1]){
              dp[i+1][j][k][(d + 1)%P] = max(dp[i+1][j][k][(d + 1)%P], dp[i][j][k][d] + bonus);
            }
            if(j+1 <= K[2]){
              dp[i][j+1][k][(d + 2)%P] = max(dp[i][j+1][k][(d + 2)%P], dp[i][j][k][d] + bonus);
            }
            if(k+1 <= K[3]){
              dp[i][j][k+1][(d + 3)%P] = max(dp[i][j][k+1][(d + 3)%P], dp[i][j][k][d] + bonus);
            }

          }
        }
      }
    }

    int tmp = 0;
    for (int d = 0; d < 4; d++) {
      tmp = max(tmp, dp[K[1]][K[2]][K[3]][d]);
    }

    printf("Case #%d: %d\n", testCase, ans + tmp);

  }

  return 0;
}
