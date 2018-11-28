#ifdef __GNUC__

#include <bits/stdc++.h>
using namespace std;

// #include <bits/extc++.h>
// using namespace __gnu_cxx;
// using namespace __gnu_pbds;

#include <ext/algorithm>
#include <ext/numeric>
#include <ext/rope>
using namespace __gnu_cxx;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/trie_policy.hpp>
using namespace __gnu_pbds;

#if __cplusplus >= 201402L
#include <experimental/numeric>
#include <experimental/string_view>
using namespace std::experimental;
#endif

#else

#include <cmath>
#include <cstdio>
#include <iostream>
#include <limits>
#include <utility>
#include <vector>
using namespace std;

#endif

#define endl '\n'
#define fi first
#define se second
#define ALL(C) std::begin(C), std::end(C)

using LL = long long;
using Pii = std::pair<int, int>;
using Vi = std::vector<int>;
using VVi = std::vector<Vi>;

constexpr auto eps = 1.0e-9;
const auto pi = std::acos(-1.0);

constexpr auto k7 = 1000 * 1000 * 1000 + 7;
constexpr auto k9 = 1000 * 1000 * 1000 + 9;
constexpr auto inf = std::numeric_limits<int>::max();


int main(int argc, char* argv[]) {
#ifndef ONLINE_JUDGE
  if (argc > 1) freopen(argv[1], "rt", stdin);
  if (argc > 2) freopen(argv[2], "wt", stdout);
#endif  // ONLINE_JUDGE
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.setf(ios::fixed);
  cout.precision(9);

  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    int n, k;
    cin >> n >> k;
    vector<Pii> ps(n+1);
    for (int i = 1; i <= n; ++i) {
      cin >> ps[i].fi >> ps[i].se;
    }
    sort(next(begin(ps), 1), end(ps), greater<Pii>());

    vector<vector<double>> dyn(k+1, vector<double>(n+1));
    dyn[1][1] = pi * ps[1].fi * ps[1].fi + 2 * pi * ps[1].fi * ps[1].se;   
    for (int i = 2; i <= n; ++i) {
      double var = pi * ps[i].fi * ps[i].fi + 2 * pi * ps[i].fi * ps[i].se;
      dyn[1][i] = max(dyn[1][i-1], var);
    }

    for (int ki = 2; ki <= k; ++ki) {
      for (int ni = ki; ni <= n; ++ni) {
        dyn[ki][ni] = max(dyn[ki][ni-1], dyn[ki-1][ni-1] + 2 * pi * ps[ni].fi * ps[ni].se);        
      }
    }
    
    cout << "Case #" << i << ": " << dyn[k][n] << endl;
  }

  return 0;
}
