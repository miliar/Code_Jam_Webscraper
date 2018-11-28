/* Copyright 2017 Yusuf Hussein
 */
#include <iostream>
#include <string>
#include <queue>

std::string solve(std::string s) {
  int len = s.size();
  for (int i = 0; i + 1< len; ++i) {
    if (s[i] > s[i + 1]) {
      while (i && s[i] == s[i - 1]) {
        --i;
      }
      --s[i];
      for (int j = i + 1; j < len; ++j) {
        s[j] = '9';
      }
      if (s[i] == '0') {
        s.erase(i, 1);
      }
      break;
    }
  }
  return s;
}

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    std::string s;
    std::cin >> s;
    std::cout << "Case #" << t << ": " << solve(s) << '\n';
  }
}
