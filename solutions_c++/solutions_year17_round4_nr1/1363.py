#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <cassert>

int main() {
  int T;
  std::cin >> T;
  for (int t = 0; t < T; ++t) { 
    int n;
    int p;
    std::cin >> n >> p;
    std::vector<int> g(p, 0);
    for (int i = 0; i < n; ++i) {
      int gi;
      std::cin >> gi;
      ++g[gi % p];
    }
    int res = 0;
    int used = 0;
    if (p == 2) {
      res = g[0] + g[1] / 2;
      used = g[0] + 2 * (g[1] / 2);
    }
    else if (p == 3) {
      const int pairs = std::min(g[1], g[2]);
      const int rest = std::max(g[1], g[2]) - pairs;
      res = g[0] + pairs + rest / 3; 
      used = g[0] + 2 * pairs + 3 * (rest / 3);
    }
    else if (p == 4) {
      const int pairs = std::min(g[1], g[3]);
      const int twos = g[2] / 2; 
      int rest = 2 * (g[2] % 2) + std::max(g[1], g[3]) - pairs;
      res = g[0] + twos + pairs + rest / 4;
      used = g[0] + 2 * pairs + 2 * twos + 4 * (rest / 4);
      if (rest >= 4)
        used -= (g[2] % 2);
    }
    if (used < n)
      ++res;
    assert(used <= n);
    

    std::cout << "Case #" << t+1 << ": " << res << std::endl;
  }
  return EXIT_SUCCESS;
}
