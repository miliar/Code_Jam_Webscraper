#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <locale>
#include <iostream>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <valarray>
#include <vector>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using ll = long long;
using ld = long double;

template <typename T> T &chmin(T &a, const T &b) { return a = std::min(a, b); }
template <typename T> T &chmax(T &a, const T &b) { return a = std::max(a, b); }
template <typename T> int len(const T &x) { return x.size(); }

template<typename T> constexpr T inf;
template<> constexpr int inf<int> = 1e9;
template<> constexpr ll inf<ll> = 1e18;
template<> constexpr ld inf<ld> = 1e30;

struct yes_no : std::numpunct<char> {
  string_type do_truename()  const { return "Yes"; }
  string_type do_falsename() const { return "No"; }
};

using namespace std;

void output(string s) {
  static int c;
  ++c;
  printf("Case #%d: %s\n", c, s.c_str());
}

int main() {
  int Q;
  cin >> Q;
  while (Q--) {
    map<ll,ll> ma;
    ll n, k;
    cin >> n >> k;
    ma[-(n + 1)] = 1;
    for (auto it = begin(ma);; ++it) {
      ll dist = -(it->first);
      ll cnt = it->second;
      ll near = dist / 2;
      ll far = dist - near;
      if (k <= cnt) {
        output(to_string(far - 1) + " " + to_string(near - 1));
        break;
      }
      k -= cnt;
      ma[-near] += cnt;
      ma[-far] += cnt;
    }
  }
  return 0;
}
