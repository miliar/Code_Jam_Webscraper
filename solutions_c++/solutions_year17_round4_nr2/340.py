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

const int N = 1000 + 10;

int sum[N], positions[N], bought[N];
int n, m, c;

void Init() {
  memset(positions, 0, sizeof(positions));
  memset(bought, 0, sizeof(bought));
}

int main() {
  int test;
  scanf("%d", &test);
  for (int t = 1; t <= test; ++ t) {
    Init();
    scanf("%d%d%d", &n, &c, &m);

    int rides = 0;
    for (int i = 1; i <= m; ++ i) {
      int x, y;
      scanf("%d%d", &x, &y);
      positions[x] ++;
      bought[y] ++;
      rides = std::max(rides, bought[y]);
    }
    for (int i = 1; i <= n; ++ i) {
      sum[i] = sum[i - 1] + positions[i];
      rides = std::max(rides, (sum[i] + i - 1) / i);
    }

    int changes = 0;
    for (int i = 1; i <= n; ++ i) {
      if (positions[i] - rides > 0) {
        changes += positions[i] - rides;
      }
    }
    printf("Case #%d: %d %d\n", t, rides, changes);
  }
  return 0;
}
