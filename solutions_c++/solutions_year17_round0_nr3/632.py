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
    std::cout << std::endl;
  }

  return 0;
}

int main() {
  return cj([]() {
    uint64_t n, k;
    std::cin >> n >> k;

    if (k > 1) {
      uint64_t
        a = (n - 1) / 2, na = 1,
        b = n / 2, nb = 1;

      uint64_t done = 1;
      while (true) {
        done += nb;
        if (done >= k) {
          n = b;
          break;
        }

        done += na;
        if (done >= k) {
          n = a;
          break;
        }

        if (a == b) {
          na *= 2;
          nb *= 2;
        }
        else { // a + 1 == b
          if (a % 2 == 1) {
            na = 2 * na + nb;
          }
          else {
            nb = 2 * nb + na;
          }
        }
        a = (a - 1) / 2;
        b = b / 2;
      }
    }

    std::cout << n / 2 << ' ' << (n - 1) / 2;
  });
}
