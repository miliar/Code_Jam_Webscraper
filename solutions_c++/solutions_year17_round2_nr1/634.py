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

pair<long double, llong> pairs[1024];

int main() {
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);
  int n_cases;
  scanf("%d", &n_cases);
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    llong d;
    int n;
    scanf("%lld %d", &d, &n);
    for (int i = 0; i < n; ++i) {
      scanf("%Lf %lld", &pairs[i].first, &pairs[i].second);
    }
    sort(pairs, pairs+n);
    pairs[n].first = d;
    pairs[n].second = 0;
    long double time = 0;
    int iter = 0;
    while (true) {
      long double soonest = 1e20;
      int soonest_idx = 0;
      bool found = false;
      for (int i = 0; i < n; ++i) {
        long double kilo;
        llong speed;
        tie(kilo, speed) = pairs[i];
        long double kilo2;
        llong speed2;
        tie(kilo2, speed2) = pairs[i+1];
        if (kilo == kilo2) continue;

        if (speed > speed2) {
          found = true;
          long double intersect = (kilo - kilo2)/(long double)(speed2 - speed);
          if (soonest > intersect) {
            soonest_idx = i;
            soonest = intersect;
          }
        }
      }
      if (!found) break;
      #ifdef DEBUG
      printf("soonest: %Lf\n", soonest);
      printf("soonest_idx: %d\n", soonest_idx);
      #endif
      #ifdef DEBUG
      puts("======");
      for (int i = 0; i <n+1; ++i) {
        printf("%d: (%Lf, %lld)\n",i, pairs[i].first, pairs[i].second);
      }
      puts("-------");
      #endif

      for (int i = 0; i < n; ++i) {
        pairs[i].first = min((long double)d, pairs[i].first + pairs[i].second * soonest);
      }
      #ifdef DEBUG
      puts("======");
      puts("POST");
      for (int i = 0; i <n+1; ++i) {
        printf("%d: (%Lf, %lld)\n",i, pairs[i].first, pairs[i].second);
      }
      puts("-------");
      #endif
      sort(pairs, pairs+n);
      for (int i = 0; i < n; ++i) {
        if (abs(pairs[i].first - pairs[i+1].first) < 1e-7) {
          llong slowest = min(pairs[i].second, pairs[i+1].second);
          pairs[i].second = pairs[i+1].second = slowest;
          pairs[i].first = pairs[i+1].first;
        }
      }

      for (int i = 0; i < n; ++i) {
        if (pairs[i].first > pairs[i+1].first) {
          fprintf(stderr, "iter %d: wtf: %d: (%Lf ; %lld) ; %d: (%Lf ; %lld)\n", iter, i, pairs[i].first, pairs[i].second, i+1, pairs[i+1].first, pairs[i+1].second);
          exit(1);
        }
      }
      time += soonest;
      ++iter;
    }
    
    printf("Case #%d: %.6Lf\n", ctr+1, d/time);
  }
  return 0;
}
