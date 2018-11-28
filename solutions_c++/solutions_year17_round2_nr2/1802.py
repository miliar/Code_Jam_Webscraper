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


const char* S = "RYB";


int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  int T, N, R, O, Y, G, B, V;

  std::cin >> T;

  for (int t = 1; t <= T; t ++) {
    std::cin >> N >> R >> O >> Y >> G >> B >> V;

    assert(O == 0 && G == 0 && V == 0);

    std::vector<std::pair<int, int>> a = {
      {R, 0},
      {Y, 1},
      {B, 2}
    };

    std::sort(ALL(a));

    int c0 = a[0].first,  c1 = a[1].first,  c2 = a[2].first;
    int i0 = a[0].second, i1 = a[1].second, i2 = a[2].second;

    int d21 = c2 - c1;

    if (d21 > 0)
      if (c0 < d21) {
        std::cout << "Case #" << t << ": IMPOSSIBLE" << std::endl;

        continue;
      }

      std::string s;

      while (c1 > 0 || c2 > 0) {
        if (c1 > 0) {
          s.push_back(S[i1]);

          c1 --;
        }

        if (c2 > 0) {
          s.push_back(S[i2]);
          
          c2 --;
        }
      }

      for (int i = 0; i < c0; i ++)
        s.insert(std::end(s) - i * 2 - 1, S[i0]);

      std::cout << "Case #" << t << ": " << s << std::endl;
  }

  return 0;
}
