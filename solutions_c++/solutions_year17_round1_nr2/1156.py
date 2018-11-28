#include <bits/stdc++.h>

using namespace std;

int T, N, P, R[2], Q[2][8], memo[8][8];

int solve(int i, int j) {
  if (i >= P || j >= P) return 0;
  if (memo[i][j] != -1) return memo[i][j];
  int c1 = round(Q[0][i] * 1.0 / R[0]);
  int c2 = round(Q[1][j] * 1.0 / R[1]);
  for (int c = min(c1, c2); c <= max(c1, c2); ++c) {
    double p1 = Q[0][i] / (c * 1.0 * R[0]);
    double p2 = Q[1][j] / (c * 1.0 * R[1]);
    if (p1 < 0.9 || p1 > 1.1) {
      continue;
    }
    if (p2 < 0.9 || p2 > 1.1) {
      continue;
    }
    return memo[i][j] = 1 + solve(i + 1, j + 1);
  }
  return memo[i][j] = max(solve(i + 1, j + 1), max(solve(i + 1, j), solve(i, j + 1)));
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);


  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    cin >> N >> P;
    for (int i = 0; i < N; ++i) {
      cin >> R[i];
    }
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < P; ++j) {
        cin >> Q[i][j];
      }
      sort(Q[i], Q[i] + P);
    }
    if (N == 1) {
      int result = 0;
      for (int j = 0; j < P; ++j) {
        double p = Q[0][j] / (round(Q[0][j] * 1.0 / R[0]) * R[0]);
        if (p >= 0.9 && p <= 1.1) {
          ++result;
        }
      }
      cout << result << '\n';
    } else {
      memset(memo, -1, sizeof(memo));
      int result = solve(0, 0);
      cout << result << '\n';
    }
  }
}