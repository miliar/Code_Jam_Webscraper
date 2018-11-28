#include <bits/stdc++.h>

#define debugf(a, ...) fprintf(stderr, a, ##__VA_ARGS__)

void debug() {
  std::cerr << "\n";
}
template<typename Head, typename... Args>
void debug(const Head& head, const Args&... args) {
  std::cerr << head << " ";
  debug(args...);
}

const int N = 100 + 10;

int g[N], dp[N][N][N][N], n, p;

int work2() {
  int even = 0;
  for (int i = 1; i <= n; ++ i) {
    even += g[i] % 2 == 0;
  }
  int result = 0;
  result += even;
  int odd = n - even;
  result += (odd + 1) / 2;
  return result;
}

int work3() {
  int result = 0;
  int mod[3] = {0, 0, 0};
  for (int i = 1; i <= n; ++ i) {
    mod[g[i] % 3] ++;
  }
  result += mod[0];
  int x = std::min(mod[1], mod[2]);
  result += x;
  mod[1] -= x;
  mod[2] -= x;
  if (mod[1] > 0) {
    result += (mod[1] + 2) / 3;
  } else {
    result += (mod[2] + 2) / 3;
  }
  return result;
}

int Update(int& a, int b) {
  if (b > a) a = b;
}

int work4() {
  int result = 0;
  int mod[4] = {0, 0, 0, 0};
  for (int i = 1; i <= n; ++ i) {
    mod[g[i] % 4] ++;
  }
  result += mod[0];

  int sum = mod[1] + mod[2] * 2 + mod[3] * 3;
  memset(dp, 0, sizeof(dp));
  dp[mod[1]][mod[2]][mod[3]][0] = 0;
  for (int a = mod[1]; a >= 0; -- a) {
    for (int b = mod[2]; b >= 0; -- b) {
      for (int c = mod[3]; c >= 0; --c) {
        for (int x = 0; x <= 3; ++ x) {
          // if (dp[a][b][c][x] == 0) continue;
          // debug(a, b, c, x, dp[a][b][c][x]);
          if (a > 0) {
            int next = (x + 1) % 4;
            Update(dp[a - 1][b][c][next], dp[a][b][c][x] + (x == 0));
          }
          if (b > 0) {
            int next = (x + 2) % 4;
            Update(dp[a][b - 1][c][next], dp[a][b][c][x] + (x == 0));
          }
          if (c > 0) {
            int next = (x + 3) % 4;
            Update(dp[a][b][c - 1][next], dp[a][b][c][x] + (x == 0));
          }
        }
      }
    }
  }

  // debug("dp", dp[0][0][0][sum % 4]);
  result += dp[0][0][0][sum % 4];
  return result;
}

int main() {
  int test;
  scanf("%d", &test);
  for (int t = 1; t <= test; ++ t) {
    scanf("%d%d", &n, &p);
    for (int i = 1; i <= n; ++ i) {
      scanf("%d", g + i);
    }
    int answer = 0;
    if (p == 2) {
      answer = work2();
    } else if (p == 3) {
      answer = work3();
    } else if (p == 4) {
      answer = work4();
    }
    printf("Case #%d: %d\n", t, answer);
  }
  return 0;
}