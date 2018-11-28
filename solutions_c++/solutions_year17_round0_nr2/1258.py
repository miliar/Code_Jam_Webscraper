#include <algorithm>
#include <iostream>
#include <string>

void ToLastTidy(std::string &s) {
  for (size_t i = 0; s[i] && s[i + 1]; ++i) {
    if (s[i] > s[i + 1]) {
      --s[i];
      for (size_t j = i + 1; s[j]; ++j) {
        s[j] = '9';
      }
      if (!i && (s[i] == '0')) {
        s = s.substr(1);
      }
      ToLastTidy(s);
    }
  }
}

int main() {
  size_t T;
  std::cin >> T;
  for (size_t t = 1; t <= T; ++t) {
    std::string s;
    std::cin >> s;
    ToLastTidy(s);
    std::cout << "Case #" << t << ": " << s << "\n";
  }
  return 0;
}
