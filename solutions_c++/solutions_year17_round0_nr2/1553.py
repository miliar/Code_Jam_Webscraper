#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstdint>
#include <vector>
#include <algorithm>

std::string solve(int64_t n);

int main() {
    int T;
    std::cin >> T;
    for (int t=1; t<=T; ++t) {
        int64_t n;
        std::cin >> n;

        std::cout << "Case #" << t << ": " << solve(n) << std::endl;
    }
    return 0;
}

size_t untidy(const std::string& s) {
  for (size_t i = 1; i < s.size(); ++i) {
    if (s[i-1] > s[i]) return i;
  }
  return s.size();
}

bool isTidy(const std::string& s) {
  return (untidy(s) == s.size());
}

struct Pow10 {
  Pow10() {
    int64_t v = 1;
    for (int i=0; i < 19; ++i) {
      p[i] = v;
      v *= 10;
    }
  }

  int64_t operator()(size_t k) { return p[k]; }

  int64_t p[19];
} pow10;

std::string solve(int64_t n) {
  int64_t cur = n;
  std::string str = std::to_string(cur);

  while (true) {
    size_t bad = untidy(str);

    if (bad == str.size()) break;
    
    size_t pos = str.size() - (bad + 1);

    int64_t mod = pow10(pos + 1);

    cur -= (cur % mod) + 1;
    str = std::to_string(cur);

    // std::clog << cur << std::endl;
  }

  return str;
}
 
