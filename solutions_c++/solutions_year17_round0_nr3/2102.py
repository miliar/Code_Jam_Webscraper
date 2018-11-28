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

#define FOR_EDGE(adj,v,it) for (EdgeList::iterator it = adj[v].begin(); \
    it != adj[v].end(); ++it)
#define FOR(v, it) for (auto it = v.begin(); it != v.end(); ++it)

int main() {
  
  int n_cases;
  scanf("%d", &n_cases);

  for (int ctr = 0; ctr < n_cases; ++ctr) {
    ullong n, k;
    scanf("%llu %llu", &n, &k);

    map<ullong, ullong> counts;
    counts[n] = 1;

    ullong splits = 0;
    ullong final_left = 0;
    ullong final_right = 0;
    while (splits < k) {
      ullong val;
      ulong count;
      auto it = counts.crbegin();
      tie(val, count) = *it;
      if (splits + count < k) {
        splits += count;
        counts.erase(--it.base());
        ullong left = (val-1)/2;
        ullong right = val/2;
        counts[left] += count;
        counts[right] += count;
      } else {
        final_left = (val-1)/2;
        final_right = (val)/2;
        break;
      }
    }
    printf("Case #%d: %llu %llu\n", ctr+1, final_right, final_left);
  }
  return 0;
}
