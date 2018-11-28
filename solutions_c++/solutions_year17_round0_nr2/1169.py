#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>
#include <numeric>
#include <functional>

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    std::string N;
    std::cin >> N;

    auto ans = N;
    size_t p = 0;
    for (size_t i = 1; i < N.size(); ++i) {
      if (N[i - 1] > N[i]) {
        --N[p];
        for (size_t j = p + 1; j < N.size(); ++j) {
          N[j] = '9';
        }
        if (N[p] == '0') {
          ans = N.substr(p + 1);
        } else {
          ans = N;
        }
        break;
      }
      if (N[i - 1] < N[i]) {
        p = i;
      }
    }
    std::cout << "Case #" << t << ": " << ans << std::endl;
  }
}
