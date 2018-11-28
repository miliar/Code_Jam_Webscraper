#include <iostream>

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int64_t N;
    std::cin >> N;
    while (true) {
      int64_t i, n;
      for (i = 10, n = N; 
          n > 0 && n % 10 >= n % 100 / 10; i *= 10) {
        n /= 10;
      }
      if (n == 0) break;
      N = N / i * i - 1;
    }
    std::cout << "Case #" << t << ": " <<  N << "\n";
  }
  return 0;
}
