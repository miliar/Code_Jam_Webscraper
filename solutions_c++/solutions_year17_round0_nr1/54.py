#include <iostream>
#include <vector>
#include <string>

char flip (const char c) {
  if (c == '-')
    return '+';
  else
    return '-';
}

int main() {
  int T;
  std::cin >> T;
  for (int t = 0; t < T; ++t) {
    std::string s;
    int k;
    std::cin >> s >> k;
    int n = s.size();
    int nflips = 0;
    for (int i = 0; i < n+1-k; ++i) {
      if (s[i] == '-') {
        for (int j = i; j < i+k; ++j)
          s[j] = flip(s[j]);
        ++nflips;
      }
    }
    std::string result = std::to_string(nflips);
    for (int i = n+1-k; i < n; ++i) {
      if (s[i] == '-')
        result = "IMPOSSIBLE";
    }

    std::cout << "Case #" << t+1 << ": " << result << std::endl;
  }
  return EXIT_SUCCESS;
}
