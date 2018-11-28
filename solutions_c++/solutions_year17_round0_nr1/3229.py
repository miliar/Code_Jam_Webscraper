#include <iostream>
#include <string>
int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    std::string S;
    int K, i, c = 0;
    std::cin >> S >> K;
    for (char& c : S) c = c == '+';
    for (i = 0; i < int(S.size()) - K + 1; ++i) {
      if (S[i]) continue;
      ++c;
      for (int j = i; j < i + K; ++j) {
        S[j] = !S[j];
      }
    }
    std::cout << "Case #" << t << ": ";
    for (; i < int(S.size()); ++i) {
      if (!S[i]) {
        std::cout << "IMPOSSIBLE\n";
        break;
      }
    }
    if (i == int(S.size()))
      std::cout << c << "\n";
  }
  return 0;
}
