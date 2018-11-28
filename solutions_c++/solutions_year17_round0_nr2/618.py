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
    std::cin >> s;

    std::vector<int> v;
    for (char c : s) {
      v.push_back(c - '0');
    }

    int i;
    int p = 0;
    for (i = 0; i < v.size(); i++) {
      if (v[i] < p) {
        break;
      }
      p = v[i];
    }

    if (i < v.size()) { // not tidy
      int j = i - 1;
      while ((j > 0) && (v[j] == v[j - 1])) {
        j--;
      }
      v[j]--;
      for (int k = j + 1; k < v.size(); k++) {
        v[k] = 9;
      }
    }

    std::reverse(std::begin(v), std::end(v));
    uint64_t n = 0, a = 1;
    for (int d : v) {
      n += d * a;
      a *= 10;
    }

    std::cout << n;
  });
}
