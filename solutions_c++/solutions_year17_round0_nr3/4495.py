#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

template<class T>
ostream& operator<< (ostream& fout, const vector<T>& vec) {
  for (const auto& el : vec) {
    fout << el << ' ';
  }
  return fout;
}

template <class T>
istream& operator>> (istream& fin, vector<T>& vec) {
  for (size_t i = 0; i < vec.size(); ++i) {
    cin >> vec[i];
  }
  return fin;
}

using ll = int64_t;
map<pair<ll, int>, map<ll, ll>> dp;
map<ll, ll> Dp(ll arg, int layer) {
  if (arg == 0) return {};
  if (layer == 0) return {{arg, 1}};
  if (dp.count({arg, layer})) {
    return dp[{arg, layer}];
  }

  ll left = (arg - 1) / 2;
  ll right = arg / 2;
  auto l = Dp(left, layer - 1);
  auto r = Dp(right, layer - 1);
  for (auto& el : r) {
    l[el.first] += el.second;
  }
  dp[{arg, layer}] = l;
  return l;
}

int Solve() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    int layer = 0;
    ll val = 0;
    ll n;
    cin >> n;
    ll len = 0;
    cin >> len;
    --len;
    while (val < len) {
      ++layer;
      val = val + (1LL << layer);
    }
    auto res =  Dp(n, layer);
    dp.clear();
    int offset = (1LL << layer) - (val - len) - 1;
    ll psum = 0;
    for (auto it = res.rbegin(); it != res.rend(); ++it) {
      auto el = *it;
      psum += el.second;
      if (psum > offset) {
        cout << "Case #" << t << ": ";
        cout << el.first / 2 << ' ' << (el.first - 1) / 2 << '\n';
        break;
      }
    }
  }
  return 0;
}


int main() {
#ifndef LOCAL
  //freopen("input.txt", "rt", stdin);
  //freopen("output.txt", "wt", stdout);
#endif
#ifdef LOCAL
  //freopen("input.txt", "rt", stdin);
#endif

  ios_base::sync_with_stdio(0);
  cin.tie(0);
  Solve();
  return 0;
}
