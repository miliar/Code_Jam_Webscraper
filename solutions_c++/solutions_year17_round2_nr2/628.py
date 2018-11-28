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
#include <boost/format.hpp>

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

constexpr int n_colors = 3;
map<int,int> colors;
int num_colors[6];
int ring[1024];

char color_names[7] = "RYBOGV";

int main() {
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);
  int n_cases;
  scanf("%d", &n_cases);
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    int n, r, o, y, g, b, v;
    scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
    fill(ring, ring+n, -1);
    num_colors[0] = r;
    num_colors[1] = y;
    num_colors[2] = b;
    num_colors[3] = o;
    num_colors[4] = g;
    num_colors[5] = v;

    #ifdef DEBUG
    printf("RING: ");
    for (int i = 0; i < n; ++i) {
      printf("%d ", ring[i]);
    }
    puts("");
    printf("NUM COLORS: ");
    for (int i = 0; i < n_colors; ++i) {
      printf("%d ", num_colors[i]);
    }
    puts("");
    #endif

    bool good = true;
    int first_color = -1;
    for (int i = 0; i < n; ++i) {
#ifdef DEBUG
      puts("-----");
      printf("ITER %d\n", i);
      printf("RING: ");
      for (int q = 0; q < n; ++q) {
        printf("%d ", ring[q]);
      }
      puts("");
      printf("NUM COLORS: ");
      for (int q = 0; q < n_colors; ++q) {
        printf("%d ", num_colors[q]);
      }
      puts("");
#endif
      int best = -1;
      int best_idx = -1;
      for (int j = 0; j < n_colors; ++j) {
        if (num_colors[j] && (i == 0 || ring[i-1] != j)) {
          if (num_colors[j] > best || (num_colors[j] == best && j == first_color)) {
            best = num_colors[j];
            best_idx = j;
          }
        }
      }
      if (best == -1) {
        good = false;
        break;
      } else {
        if (i == 0) first_color = best_idx;
        --num_colors[best_idx];
        ring[i] = best_idx;
      }
    }
    if (ring[n-1] == ring[0]) good = false;
    if (!good) printf("Case #%d: IMPOSSIBLE\n", ctr+1);
    else {
      printf("Case #%d: ", ctr+1);
      for (int i = 0; i < n; ++i) {
        printf("%c", color_names[ring[i]]);
      }
      puts("");
    }
  }
  return 0;
}
