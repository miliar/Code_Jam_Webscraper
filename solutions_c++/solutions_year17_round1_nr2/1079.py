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

int n;
int p;
llong rats[64];
llong packs[64][64];
bool taken[64];
int best;

typedef pair<long, long> pll ;
pll portion_range(llong package, llong ration) {
  return make_pair((llong)(ceil(10*package/(double)(11*ration))),
                   (llong)floor(10*package/(double)(9*ration)));
}

pll intersect_range(pll& a, pll& b) {
  return make_pair(max(a.first, b.first), min(a.second, b.second));
}

void recurse(int idx) {
  if (idx == p) {
    best = max(best, accumulate(taken, taken+p, 0));
    return;
  }
  recurse(idx+1);
  pll aport = portion_range(packs[0][idx], rats[0]);
  for (int i = 0; i < p; ++i) {
    if (taken[i]) continue;
    pll bport = portion_range(packs[1][i], rats[1]);
    pll inter = intersect_range(aport, bport);
    if (inter.first <= inter.second) {
      taken[i] = true;
      recurse(idx+1);
      taken[i] = false;
    }
  }
}

int main() {
  int n_cases;
  scanf("%d", &n_cases);
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    cin >> n >> p;
    for (int i = 0; i < n; ++i) {
      cin >> rats[i];
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < p; ++j) {
        cin >> packs[i][j];
      }
    }

    if (n == 2) {
      memset(taken, 0, sizeof(taken));
      best = 0;
      recurse(0);
    } else {
      best = 0;
      for (int i = 0; i < p; ++i) {
        pll range = portion_range(packs[0][i], rats[0]);
        if (range.first <= range.second) {
          ++best;
        }
      }
    }

    cout << "Case #" << ctr+1 << ": " << best << endl;
  }
  return 0;
}
