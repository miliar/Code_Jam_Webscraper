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

  for (int t = 1; t <= T; t ++) {
    long long N;

    std::cin >> N;

    std::string s(std::to_string(N));

    while (1) {
      for (int i = 0, size = s.size(); i < size - 1; i ++)
        if (s[i] <= s[i + 1]) {
          ;
        }
        else {
          assert(s[i] >= '1');

          s = s.substr(0, i + 1) + std::string(size - i - 1, '9');

          s[i] --;

          while (s.front() == '0')
            s = s.substr(1);

          goto next;
        }

      break;

    next: ;
    }

    std::cout << "Case #" << t << ": " << s << std::endl;
  }

  return 0;
}
