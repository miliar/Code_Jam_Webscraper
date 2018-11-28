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

  int T, K;

  std::string s;

  std::cin >> T;

  for (int t = 1; t <= T; t ++) {
    std::cin >> s >> K;

    int c = 0;

    for (int i = 0, size = s.size(); i < size; i ++) {
      if (i + K - 1 == size)
        break;
      
      if (s[i] == '-') {
        for (int j = 0; j < K; j ++)
          s[i + j] = s[i + j] == '-' ? '+' : '-';

        c ++;
        
#if 0
        std::cerr << s << std::endl;
#endif
      }
    }

    if (s.find('-') == std::string::npos) {
      std::cout << "Case #" << t << ": " << c << std::endl;
    }
    else {
      std::cout << "Case #" << t << ": IMPOSSIBLE" << std::endl;
    }
  }

  return 0;
}
