#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int D, N;
    std::cin >> D >> N;
    std::vector<double> h(N);
    for (int i = 0; i < N; ++i) {
      int k, s;
      std::cin >> k >> s;
      h[i] = double(D - k) / s;
    }
    std::sort(h.begin(), h.end());
    std::cout << "Case #" << t << ": " 
      << std::fixed << std::setprecision(6) << D / h[N - 1] << "\n";
  }
  return 0;
}
