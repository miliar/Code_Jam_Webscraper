#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <array>
#include <algorithm>
#include <cstdio>
#include <cstdint>
#include <cassert>
#include <string>

template <typename F>
int cj(F const& f) {
  int t;
  std::cin >> t;

  for (int i = 1; i <= t; i++) {
    std::cout << "Case #" << i << ": ";
    f();
    std::cout << std::endl;
  }

  return 0;
}

int main() {
  return cj([]() {
    std::string s;
    int k;
    std::cin >> s >> k;

    std::vector<bool> v;
    for (auto c : s) {
      v.push_back(c == '+');
    }

    int f = 0, n = v.size();
    for (auto i = 0; i <= n - k; i++) {
      if (!v[i]) {
        f++;
        for (auto j = i; j < i + k; j++) {
          v[j] = !v[j];
        }
      }
    }

    bool ok = true;
    for (auto a : v) {
      if (!a) {
        ok = false;
        break;
      }
    }

    if (ok) {
      std::cout << f;
    }
    else {
      std::cout << "IMPOSSIBLE";
    }
  });
}
