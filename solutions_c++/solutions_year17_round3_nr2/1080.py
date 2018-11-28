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
  node_t(int ll, int rr) : l(ll), r(rr) {};

public:
  int length() const {
    if (r >= l) {
      return r - l;
    }
    else {
      return r - l + 1440;
    }
  };

public:
  bool operator<(const node_t& x) const {
    int d = length(), dd = x.length();

    if (d == dd)
      return l < x.l;

    return d < dd;
  };

  bool operator>(const node_t& x) const {
    return ! (*this < x);
  };

public:
  int l;
  int r;
};


int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  int T, Ac, Aj, C, D, J, K;

  std::cin >> T;

  for (int t = 1; t <= T; t ++) {
    bool debug = t == 67;
    
    std::cin >> Ac >> Aj;

    int c[2] = {0};

    std::vector<int> a(1440, -1), evc, evj;

    for (int i = 0; i < Ac; i ++) {
      std::cin >> C >> D;

      std::fill(std::begin(a) + C, std::begin(a) + D, 0);

      c[0] += D - C;
    }

    for (int i = 0; i < Aj; i ++) {
      std::cin >> J >> K;

      std::fill(std::begin(a) + J, std::begin(a) + K, 1);

      c[1] += K - J;
    }

    std::priority_queue<node_t, std::vector<node_t>, std::greater<node_t>> pq;

    int i, ip = 1440, l, r;

    for (i = 0; i < ip; l = r = -1) {
      for ( ; i < ip; i ++)
        if (a[i] == -1) {
          l = i;
          
          i ++;
          
          break;
        }

      if (l == -1)
        break;

      if (l == 0)
        for (int j = 1440 - 1; a[j] == -1; j --)
          ip = l = j;
      
      for (r = i; a[i] == -1 && i < ip; i ++)
        r = i;

      pq.emplace(l, r + 1);
    }

    assert(l == -1 && r == -1);

    while (! pq.empty()) {
      node_t node = pq.top(); pq.pop();

      int l = (node.l - 1 + 1440) % 1440;
      int r =  node.r             % 1440;

      assert(a[l] >= 0 && a[r] >= 0);

      if (a[l] != a[r])
        continue;

      int x = a[l];

      if (node.length() <= 720 - c[x]) {
        if (l < r) {
          std::fill(std::begin(a) + l, std::begin(a) + r, x);
        }
        else {
          std::fill(std::begin(a) + l, std::end  (a),     x);
          std::fill(std::begin(a),     std::begin(a) + r, x);
        }

        c[x] += node.length();
      }        
    }

    for (int k = 0; k < 2; k ++) {
      for (int i = 0, x; i < 1440; i ++) {
        if (i == 0)
          if (a[i] == -1) {
            int ii = 1440 - 1;
            
            if ((x = a[ii]) >= 0)
              if (c[x] < 720)
                c[a[i] = x] ++;
          }
        
        if ((x = a[i]) >= 0)
          if (c[x] < 720) {
            int ii = (i + 1) % 1440;
            
            if (a[ii] == -1)
              c[a[ii] = x] ++;
          }
      }
    
      for (int i = 1440 - 1, x; i >= 0; i --) {
        if (i == 1440 - 1)
          if (a[i] == -1) {
            int ii = 0;
            
            if ((x = a[ii]) >= 0)
              if (c[x] < 720)
                c[a[i] = x] ++;
          }
        
        if ((x = a[i]) >= 0)
          if (c[x] < 720) {
            int ii = (i - 1 + 1440) % 1440;
            
            if (a[ii] == -1)
              c[a[ii] = x] ++;
          }
      }
    }
    
    assert(c[0] == 720 || c[1] == 720);

    if (c[0] == 720) {
      for (int i = 0; i < 1440; i ++)
        if (a[i] == -1)
          c[a[i] = 1] ++;
    }
    else {
      for (int i = 0; i < 1440; i ++)
        if (a[i] == -1)
          c[a[i] = 0] ++;
    }

    assert(c[0] == 720 || c[1] == 720);

    int R = 0;

    for (int i = 0; i < 1440; i ++) {
      int ii = (i + 1) % 1440;

      if (a[i] != a[ii])
        R ++;
    }

    std::cout << "Case #" << t << ": " << R << std::endl;
  }
  
  return 0;
}
