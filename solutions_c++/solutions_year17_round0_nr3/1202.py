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
    int64_t N, K;
    std::cin >> N >> K;

    for (; K > 1;) {
      if (K % 2 == 0) {
        N /= 2;
        K /= 2;
      } else {
        N = (N - 1) / 2;
        K = (K - 1) / 2;
      }
    }
    std::cout << "Case #" << t << ": " << N / 2 << " " << (N - 1) / 2
              << std::endl;
  }
}
