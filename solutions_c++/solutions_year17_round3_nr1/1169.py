#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>

using namespace std;

const int MAXN = 1111;
const double INF = 1e10;

vector<pair<int, int> > data;
double R[MAXN], H[MAXN];
double dp[MAXN][MAXN];

int main() {
  int T;
  cin >> T;
  for (int cases = 0; cases < T; ++cases) {
    int N, K;
    cin >> N >> K;
    data.resize(N);
    for (int i = 0; i < N; ++i) {
      cin >> data[i].first >> data[i].second;
    }
    sort(data.begin(), data.end());
    for (int i = 1; i <= N; ++i) {
      R[i] = data[N - i].first;
      H[i] = data[N - i].second;
    }
    for (int i = 0; i <= N; ++i) {
      for (int j = 0; j <= N; ++j) {
        dp[i][j] = -INF;
      }
    }
    for (int i = 0; i <= N; ++i) {
      dp[i][0] = 0;
    }
    // dp[i][k] = dp[i - 1][k - 1] + h[i] * pi * r[i]^2
    for (int i = 1; i <= N; ++i) {
      for (int j = 1; j <= i; ++j) {
        if (j == 1) {
          dp[i][j] = H[i] * 2 * M_PI * R[i] + M_PI * R[i] * R[i];
        } else {
          dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + H[i] * 2 * M_PI * R[i]);
        }
        dp[i][j] = max(dp[i][j], dp[i - 1][j]);
      }
    }
    printf("Case #%d: %.10lf\n", cases + 1, dp[N][K]);
  }
}