#include <iostream>
#include <vector>
#include <algorithm>
int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int64_t N, K, y, z;
    std::cin >> N >> K;
    int64_t i, n = N, r, c = 1 - n % 2;
    for (i = 2;; i *= 2) {
      r = n % 2;
      n /= 2;
      if (i > K) break;
      if (n % 2 + r == 1) c = i - c;
      if (n <= 1) c = 0;
    }
    y = z = n;
    if (!r) --z;
    if (r && i - c <= K) --y;
    if (!r && i / 2 + c <= K) --y;
    if (y < z) std::swap(y, z);
    std::cout << "Case #" << t << ": ";
    std::cout << y << " " << z << "\n";
  }
  return 0;
}
