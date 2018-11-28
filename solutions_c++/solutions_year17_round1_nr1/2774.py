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


class node_t {
public:
  node_t(char cc, int xx0, int yy0, int xx1, int yy1) :
    c(cc), x0(xx0), y0(yy0), x1(xx1), y1(yy1), A((xx1 - xx0 + 1) * (yy1 - yy0 + 1))
  {
  };

public:
  bool operator<(const node_t& x) const {
    if (A != x.A)
      return A < x.A;

    if (c != x.c)
      return c < x.c;

    if (x0 != x.x0)
      return x0 < x.x0;

    if (y0 != x.y0)
      return y0 < x.y0;
    
    if (x1 != x.x1)
      return x1 < x.x1;

    return y1 < x.y1;
  };

  bool operator>(const node_t& x) const {
    return ! (*this < x);
  };
  
public:
  char c;
  
  int x0;
  int y0;
  int x1;
  int y1;
  
  int A;
};


int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  int T, R, C;
  
  std::cin >> T;

  for (int t = 1; t <= T; t ++) {
    std::cin >> R >> C;

    std::vector<std::string> a(R);

    for (auto& s : a)
      std::cin >> s;

    char c;

    std::priority_queue<node_t> pq;

    for (int i = 0; i < R; i ++)
      for (int j = 0; j < C; j ++)
        for (int k = i; k < R; k ++)
          for (int l = j; l < C; l ++) {
            std::set<char> set;

            for (int m = i; m <= k; m ++)
              for (int n = j; n <= l; n ++) {
                if ((c = a[m][n]) != '?') {
                  set.insert(c);

                  if (set.size() > 1)
                    goto endloop;
                }
              }

          endloop:

            if (set.size() == 1)
              pq.emplace(*set.begin(), j, i, l, k);
          }

    std::vector<std::string> b(R, std::string(C, '?'));

    bool used[33] = {0};

    while (! pq.empty()) {
      node_t node = pq.top(); pq.pop();

      if (! used[node.c - 'A']) {
        bool valid = true;
        
        for (int i = node.y0; i <= node.y1; i ++)
          for (int j = node.x0; j <= node.x1; j ++)
            if (b[i][j] != '?') {
              valid = false;

              goto endloop2;
            }

      endloop2:

        if (! valid)
          continue;

        for (int i = node.y0; i <= node.y1; i ++)
          for (int j = node.x0; j <= node.x1; j ++)
            b[i][j] = node.c;
        
        used[node.c - 'A'] = true;
      }
    }

    std::cout << "Case #" << t << ':' << std::endl;

    for (const auto& s : b)
      std::cout << s << std::endl;
  }

  return 0;
}
