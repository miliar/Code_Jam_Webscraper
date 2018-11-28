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

bool is_ok(ll n) {
  string s = to_string(n);
  int len = s.size();
  REP(i,len-1) {
    if (s[i] > s[i+1]) return false;
  }
  return true;
}

ll f(ll n) {
  if (is_ok(n)) return n;
  else return f(n / 10 - 1) * 10 + 9;
}

int main() {
  int Q;
  cin >> Q;
  while (Q--) {
    ll n;
    cin >> n;
    output(to_string(f(n)));
  }
  return 0;
}
