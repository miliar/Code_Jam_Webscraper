#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <unordered_map>
#include <vector>


#define INF 1000000002486618624LL
#define MOD 1000000007
#define ALL(x) std::begin(x), std::end(x)


int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  int T;

  std::cin >> T;

  long long N, K;

  for (int t = 1; t <= T; t ++) {
    std::cin >> N >> K;

    std::map<std::pair<long long, long long>, long long> map;

    long long m = (1 + N) / 2, a = m - 1, b = N - m;

    if (a < b)
      std::swap(a, b);

    map[std::make_pair(a, b)] = 1;
    
    std::set<std::pair<long long, long long>> keys;

    keys.emplace(a, b);

    while (! keys.empty()) {
      std::set<std::pair<long long, long long>> ks;
      
      for (const auto& key : keys) {
        if (key.first == 0 && key.second == 0)
          continue;

        for (long long x : { key.first, key.second }) {
          if (! x)
            continue;
          
          long long m = (1 + x) / 2, a = m - 1, b = x - m;

          if (a < b)
            std::swap(a, b);

          std::pair<long long, long long> k(a, b);

          map[k] += map[key];

          if (a || b)
            ks.emplace(a, b);
        }
      }

      keys = std::move(ks);
    }

    for (auto it = map.rbegin(); it != map.rend(); ++ it) {
      if (K <= it->second) {
        std::cout << "Case #" << t << ": " << it->first.first << ' ' << it->first.second << std::endl;
        
        break;
      }

      K -= it->second;
    }
  }

  return 0;
}
