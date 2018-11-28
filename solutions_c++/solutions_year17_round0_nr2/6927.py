#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <assert.h>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <tuple>
#include <algorithm>
#include <memory>
#include <utility>
#include <iostream>
#include <complex>
#include <exception>
#include <type_traits>

static uint64_t answer(const uint64_t x)
{
    if (x >= 0 && x <= 9) return x;

  std::vector<int32_t> digs;
  uint64_t t = x;
    while (t) {
        digs.push_back(t % 10);
        t /= 10;
    }

    for (int32_t i = 1; i < digs.size(); ++i) {
        if (digs[i] > digs[i-1]) {
            --digs[i];
            for (int32_t j = 0; j < i; ++j) {
                digs[j] = 9;
            }
        }
    }
  uint64_t ret = 0, pow10 = 1;
    for (int32_t i = 0; i < digs.size(); ++i) {
        ret += pow10 * digs[i];
        pow10 *= 10;
    }
  return ret;
}

int32_t main(int32_t argc, char **argv)
{
  int32_t n;
    std::cin >> n;

    for (int32_t i = 1; i <= n; ++i) {
      uint64_t x;
        std::cin >> x;
        fprintf(stdout, "Case #%d: %lu\n", i, answer(x));
    }
  return 0;
}
