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

static int32_t answer(std::string &str, const int32_t k) {
  const int32_t length = str.length();
  int32_t ret = 0;
    for (int32_t i = 0; i <= length-k; ++i) {
        if (str[i] == '+') continue;
        for (int32_t j = 0; j < k; ++j) {
            str[i+j] = str[i+j] == '-' ? '+' : '-';
        }
        ++ret;
    }

    for (int32_t i = 0; i < length; ++i) {
        if (str[i] == '-') {
          return -1;
        }
    }
  return ret;
}

int32_t main(int32_t argc, char **argv)
{
  int32_t n;
    std::cin >> n;
    for (int32_t i = 0; i < n; ++i) {
      std::string str;
      int32_t k;
        std::cin >> str >> k;
      std::string str1 = str;
        std::reverse(str1.begin(), str1.end());
      int32_t ans = answer(str, k);
      int32_t ans1 = answer(str1, k);
        if (ans == -1 && ans1 == -1) {
            fprintf(stdout, "Case #%d: IMPOSSIBLE\n", i+1);
        }
        else {
          int32_t a = std::min(ans, ans1);
            if (a == -1) {
                a = ans1 == -1 ? ans : ans1;
            }
            fprintf(stdout, "Case #%d: %d\n", i+1, a);
        }
    }
  return 0;
}
