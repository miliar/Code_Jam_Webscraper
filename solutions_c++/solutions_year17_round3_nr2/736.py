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
  cout.precision(6);

  int t;
  cin >> t;
  for (int ti = 1; ti <= t; ++ti) {
    int ac, aj;
    cin >> ac >> aj;
    int n = ac + aj;
    struct Act { int s, f, cj; };
    int t[2] = {};
    vector<Act> acts(ac+aj);
    for (int i = 0; i < ac; ++i) {
      cin >> acts[i].s >> acts[i].f;
      acts[i].cj = 0;
      t[1] += acts[i].f - acts[i].s;
    }
    for (int i = ac; i < ac + aj; ++i) {
      cin >> acts[i].s >> acts[i].f;
      acts[i].cj = 1;
      t[0] += acts[i].f - acts[i].s;
    }
    sort(ALL(acts), [](Act& x, Act& y){
        return x.s < y.s; 
      });
    int exch = 0;
    vector<Act> pause;
    for (int i = 0; i < ac + aj; ++i) {
      if (acts[i].cj != acts[(i+1)%n].cj) {
        ++exch;
      } else {
        pause.push_back({acts[i].f, acts[(i+1)%n].s, !acts[i].cj});
        if (pause.back().s > pause.back().f) {
          pause.back().f += 1440;
        }
//        int dt = acts[(i+1)%n].s - acts[i].f;
//        if (dt < 0) dt += 1440;
//        t[!acts[i].cj] += dt;
      }
    }
    sort(ALL(pause), [](Act& x, Act& y){
      return x.f - x.s < y.f - y.s;
    });
    for (int i = 0; i < pause.size(); ++i) {
      int dt = pause[i].f - pause[i].s;
      if (t[pause[i].cj] + dt <= 720) {
        t[pause[i].cj] += dt;
      } else {
        exch += 2;
      }
    }


//    for (int i = 0; i < n; ++i) {
//      if (acts[i].cj != acts[(i+1)%n].cj) {
//        int dt = acts[(i+1)%n].s - acts[i].f;
//        if (dt < 0) dt += 1440;
//        if (t[0] < t[1]) {
//          t[0] += min(t[1]-t[0], dt);
//          dt -= min(t[1]-t[0], dt);
//        } else if (t[1] < t[0]) {
//          t[1] += min(t[0]-t[1], dt);
//          dt -= min(t[0]-t[1], dt);
//        }
//        if (t[0] == t[1]) {
//          t[0] += dt / 2;
//          t[1] += (dt + 1) / 2;
//        }
//      }
//    }
//    if (t[0] != t[1]) {
//      sort(ALL(pause), [](Pii& x, Pii& y){
//          return x.se - x.fi > y.se - y.fi;
//        });
//    }
//    for (int i = 0; i  < pause.size(); ++i) {
//      if (t[0] == t[1])
//        break;
//      int dt = pause[i].se - pause[i].fi;
//      if (t[0] < t[1]) {
//        t[0] += min(t[1]-t[0], dt);
//      } else if (t[1] < t[0]) {
//        t[1] += min(t[0]-t[1], dt);
//      }
//    }

    cout << "Case #" << ti << ": " << exch << endl;
  }

  return 0;
}
