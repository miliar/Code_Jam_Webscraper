#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <queue>

using namespace std;

const int MAXN = 55;
const double eps = 1e-8;
double P[MAXN];
int U;

double dp[MAXN][MAXN * 10000];

inline int sgn(double x) {
  return x < -eps ? -1 : x > eps;
}

int main() {
  int T;
  cin >> T;
  for (int cases = 0; cases < T; ++cases) {
    int N, K;
    cin >> N >> K;
    double UU;
    cin >> UU;
    int U = int(UU * 10000 + 0.5);
    int left = 0;
    priority_queue<double, vector<double>, greater<double> > pq;
    for (int i = 1; i <= N; ++i) {
      cin >> P[i];
      int PP = int(P[i] * 10000 + 0.5);
      pq.push(P[i]);
      left += 10000 - PP;
    }
    while (sgn(UU) >= 0) {
      double smallest = pq.top();
      if (sgn(smallest - 1.0) >= 0) {
        break;
      }
      int cnt = 1;
      pq.pop();
      while (!pq.empty() && sgn(pq.top() - smallest) == 0) {
        pq.pop();
        cnt++;
      }
      double limit = 1.0;
      if (!pq.empty()) {
        limit = pq.top();
      }
      if (UU >= (limit - smallest) * cnt) {
        for (int i = 0; i < cnt; ++i) {
          pq.push(limit);
        }
        UU -= (limit - smallest) * cnt;
      } else {
        for (int i = 0; i < cnt; ++i) {
          pq.push(smallest + UU / cnt);
        }
        UU = 0;
        break;
      }
    }
    double ans = 1.0;
    while (!pq.empty()) {
      ans *= pq.top();
      pq.pop();
    }
    // dp[0][0] = 1;
    // for (int i = 1; i <= N; ++i) {
    //   for (int j = 0; j <= U; ++j) {
    //     int lower = 10000 - int(P[i] * 10000 + 0.5);
    //     for (int k = max(0, j - lower); k <= j; ++k) {
    //       dp[i][j] = max(dp[i][j], dp[i - 1][k] * (P[i] + (double(j - k) / 10000.0)));
    //     }
    //   }
    // }
    // double ans = 0;
    // for (int i = 0; i <= U; ++i) {
    //   ans = max(ans, dp[N][i]);
    // }
    printf("Case #%d: %.9lf\n", cases + 1, ans);
  }
}