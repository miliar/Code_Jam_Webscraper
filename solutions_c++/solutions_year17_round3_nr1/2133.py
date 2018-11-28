#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>
#include <numeric>
#include <functional>
#include <iomanip>

struct Node {
  int R, H;
};

double surface(const Node &a) {
  return M_PI * a.R * a.R + 2 * M_PI * a.R * a.H;
}

double exclude(int r) { return M_PI * r * r; }

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N, K;
    std::cin >> N >> K;
    std::vector<Node> v(N);
    for (auto &a : v) {
      std::cin >> a.R >> a.H;
    }
    std::sort(std::begin(v), std::end(v), [](const auto &lhs, const auto &rhs) {
      return lhs.R < rhs.R || (lhs.R == rhs.R && lhs.H < rhs.H);
    });

    auto ans = 0.0;
    for (int mask = 0; mask < (1 << 10); ++mask) {
      if (__builtin_popcount(mask) > K) {
        continue;
      }
      auto lans = 0.0;
      auto last_r = 0;
      for (int i = 0; i < (int)v.size(); ++i) {
        if (!(mask & (1 << i))) {
          continue;
        }
        lans += surface(v[i]) - exclude(last_r);
        last_r = v[i].R;
      }
      ans = std::max(ans, lans);
    }
    std::cout << "Case #" << t << ": " << std::fixed << std::setprecision(9)
              << ans << std::endl;
  }
}
