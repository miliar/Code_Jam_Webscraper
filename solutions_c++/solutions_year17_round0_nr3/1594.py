#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstdint>
#include <vector>
#include <map>
#include <algorithm>

std::string solve(uint64_t n, uint64_t k);

int main() {
    int T;
    std::cin >> T;
    for (int t=1; t<=T; ++t) {
        uint64_t n, k;
        std::cin >> n >> k;

        std::cout << "Case #" << t << ": " << solve(n, k) << std::endl;
    }
    return 0;
}

using Levels = std::vector<std::map<uint64_t, uint64_t>>;

Levels makeLevels(uint64_t n) {
  Levels lev;
  lev.push_back({{n, 1}});

  while (true) {
    std::map<uint64_t, uint64_t> next;

    const auto& prev = lev.back();

    for (const auto& vc : prev) {
      auto half = vc.first / 2;
      
      if (half == 0) continue;

      if (vc.first % 2 == 1) {
        next[half] += 2 * vc.second;
      } else {
        next[half] += vc.second;
        if (half > 1) {
          next[half - 1] += vc.second;
        }
      }
    }

    if (next.size() > 0)
      lev.emplace_back(std::move(next));
    else
      break;
  }

/*
  for (const auto& l : lev) {
    uint64_t choices = 0;
    for (const auto& vc : l) {
      std::clog << "{" << vc.first << ", " << vc.second << "} ";
      choices += vc.second;
    }
    std::clog << "  choices: " << choices << std::endl;
  }
//*/
  return lev;
}

std::string solve(uint64_t n, uint64_t k) {
  auto levels = makeLevels(n);

  for (size_t i=0; i<levels.size(); ++i) {
    for (auto it = levels[i].rbegin(); it != levels[i].rend(); ++it) {
      if (k <= it->second) {
        uint64_t half = it->first / 2;
        if (it->first % 2 == 1) {
          return std::to_string(half) + " " + std::to_string(half);
        } else {
          return std::to_string(half) + " " + std::to_string(half - 1);
        }
      } else {
        k -= it->second;
      }
    }
  }
  std::clog << "wait a minute...";
  return "0 0";
}
/*

1000
500 499
250 249 249 249
125 124 124 124 124 124 124 124
62 62 62 61 62 61 62 61 62 61 62 61 62 61 62 61

*/
