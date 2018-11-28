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
#include <queue>

template <typename F>
int cj(F const& f) {
  int t;
  std::cin >> t;

  for (int i = 1; i <= t; i++) {
    std::cout << "Case #" << i << ": ";
    f();
    // std::cout << std::endl;
  }

  return 0;
}

int main() {
  return cj([]() {
    int r, c;
    std::cin >> r >> c;
    std::vector<std::vector<char>> v;
    for (auto i = 0; i < r; i++) {
      std::string line;
      std::cin >> line;
      std::vector<char> row;
      for (char e : line) {
        row.push_back(e);
      }
      v.push_back(row);
    }

    for (auto& row : v) {
      char last = '?';
      for (auto i = 0; i < c; i++) {
        if (row[i] == '?') {
          row[i] = last;
        }
        else {
          if (last == '?') {
            last = row[i];
            for (auto j = i - 1; j >= 0; j--) {
              if (row[j] == '?') {
                row[j] = last;
              }
              else {
                break;
              }
            }
          }
          last = row[i];
        }
      }
    }

    int p = -1;
    for (auto j = 0; j < r; j++) {
      auto& row = v[j];
      if (row[0] == '?') {
        if (p != -1) {
          row = v[p];
        }
      }
      else {
        p = j;
      }
    }

    p = -1;
    for (auto j = r - 1; j >= 0; j--) {
      auto& row = v[j];
      if (row[0] == '?') {
        if (p != -1) {
          row = v[p];
        }
      }
      else {
        p = j;
      }
    }

    std::cout << std::endl;
    for (auto const& row : v) {
      for (char c : row) {
        std::cout << c;
      }
      std::cout << std::endl;
    }
  });
}
