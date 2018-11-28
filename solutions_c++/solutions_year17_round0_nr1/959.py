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
    string s;
    int k;
    cin >> s >> k;
    s = "+" + s + "+";
    int n = s.size();
    vector<int> v(n - 1);
    REP(i,n-1) v[i] = (s[i] != s[i+1]);
    int res = 0;
    REP(i,n-1) {
      if (v[i]) {
        int j = i + k;
        if (j >= n - 1) res = -1e9;
        else v[j] = 1 - v[j];
        ++res;
      }
    }
    if (res < 0) output("IMPOSSIBLE");
    else output(to_string(res));
  }
  return 0;
}
