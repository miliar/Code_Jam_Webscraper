#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <complex>
#include <numeric>
#include <ext/numeric>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <functional>
#include <utility>
#include <vector>
#include <list>
#include <queue>
#include <bitset>
#include <tuple>

using namespace std;
using namespace __gnu_cxx;

typedef unsigned long long ullong;
typedef long long llong;
typedef list<int> EdgeList;
typedef vector<EdgeList> AdjList;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef complex<double> Point;
#define X(p) real(p)
#define Y(p) imag(p)

#define FOR_EDGE(adj,v,it) for (EdgeList::iterator it = adj[v].begin(); \
    it != adj[v].end(); ++it)
#define FOR(v, it) for (auto it = v.begin(); it != v.end(); ++it)

int n, p;
int arr[128];
int ans;
int mod[8];
int o2[101];
int o3[101][101];
int o4[101][101][101];

int main() {
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);
  int n_cases;
  scanf("%d", &n_cases);

  p = 2;
  for (int k1 = 0; k1 <= 100; ++k1) {
    if (k1 >= 1) {
      o2[k1] = o2[k1-1] + (((k1-1)) % p == 0);
    }
  }
  p = 3;
  for (int k1 = 0; k1 <= 100; ++k1) {
    for (int k2 = 0; k2 <= 100; ++k2) {
      if (k1 >= 1) {
        o3[k1][k2] = o3[k1-1][k2] + (((k1-1) + 2*k2) % p == 0);
      }
      if (k2 >= 1) {
        o3[k1][k2] = max(o3[k1][k2], o3[k1][k2-1] + ((k1 + 2*(k2-1)) % p == 0));
      }
    }
  }
  p = 4;
  for (int k1 = 0; k1 <= 100; ++k1) {
    for (int k2 = 0; k2 <= 100; ++k2) {
      for (int k3 = 0; k3 <= 100; ++k3) {
        if (k1 >= 1) {
          o4[k1][k2][k3] = o4[k1-1][k2][k3] + (((k1-1) + 2*k2 + 3*k3) % p == 0);
        }
        if (k2 >= 1) {
          o4[k1][k2][k3] = max(o4[k1][k2][k3], o4[k1][k2-1][k3] + ((k1 + 2*(k2-1) + 3*k3) % p == 0));
        }
        if (k3 >= 1) {
          o4[k1][k2][k3] = max(o4[k1][k2][k3], o4[k1][k2][k3-1] + ((k1 + 2*k2 + 3*(k3-1)) % p == 0));
        }
      }
    }
  }
  #ifdef DEBUG
  for (int i = 0; i <= 3; ++i) {
    for (int j = 0; j <= 3; ++j) {
      printf("(%d,%d)::%d \n", i, j, o3[i][j]);
    }
    puts("");
  }
  #endif

  for (int ctr = 0; ctr < n_cases; ++ctr) {
    scanf("%d %d", &n, &p);
    for (int i = 0; i < n; ++i) {
      scanf("%d" ,&arr[i]);
    }
    ans = 0;
    memset(mod, 0, sizeof(mod));
    for (int i = 0; i < n; ++i) {
      ++mod[arr[i] % p];
    }
    if (p == 2) {
      ans = mod[0] + o2[mod[1]];
    } else if (p == 3) {
      ans = o3[mod[1]][mod[2]] + mod[0];
    } else if (p == 4) {
      ans = o4[mod[1]][mod[2]][mod[3]] + mod[0];
    }
    printf("Case #%d: %d\n", ctr+1, ans);
  }
  return 0;
}
