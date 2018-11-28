#include <cstdio>
#include <algorithm>
#include <vector>

int main() {
  int T;
  scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) {
    int n, c, m;
    scanf("%d%d%d", &n, &c, &m);
    std::vector<int> A(n + 1, 0);
    std::vector<int> R(c + 1, 0);
    for (int i = 0; i < m; ++i) {
      int P, B;
      scanf("%d%d", &P, &B);
      R[B]++;
      A[P]++;
    }
    int ret = 0;
    for (int i = 1; i <= c; ++i) {
      ret = std::max(ret, R[i]);
    }
    int sum = 0;
    for (int i = 1; i <= n; ++i) {
      sum += A[i];
      ret = std::max(ret, sum / i + !!(sum % i));
    }
    int ans = 0;
    for (int i = 1; i <= n; ++i) {
      ans += std::max(0, A[i] - ret);
    }
    printf("Case #%d: %d %d\n", cas, ret, ans);
  }
  return 0;
}
