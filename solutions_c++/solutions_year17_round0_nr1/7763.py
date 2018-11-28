#include <bits/stdc++.h>
int main() {
  int T, K;
  std::string S;
  std::cin >> T;
  for (int t = 0; t < T; t++) {
    int ans = 0;
    std::cin >> S >> K;
    for (int i = 0; i < S.size() - K + 1; i++) {
      if (S[i] == '-') {
        ans++;
        for (int k = 0; k < K; k++) {
          S[i+k] = S[i+k] == '+' ? '-' : '+';
        }
      }
    }
    std::cout << "Case #" << t+1 << ": ";
    if (S.find('-') == std::string::npos) {
      std::cout << ans << std::endl;
    } else {
      std::cout << "IMPOSSIBLE" << std::endl;
    }
  }
  return 0;
}
