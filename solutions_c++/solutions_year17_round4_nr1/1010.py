#include <bits/stdc++.h>
#include <boost/range/irange.hpp>
#include <boost/range.hpp>
#include "../../prettyprint.hpp"
using namespace std;
using boost::irange;
using boost::make_iterator_range;

#ifdef NDEBUG
#include <boost/iostreams/stream.hpp>
#include <boost/iostreams/device/null.hpp>
boost::iostreams::stream<boost::iostreams::null_sink> logs((boost::iostreams::null_sink()));
#else
auto& logs = cerr;
#endif

array<map<tuple<int, int, int, int>, int>, 5> memo;
int dp(int p, int sum, int c1, int c2, int c3) {
  if (c1<0) return 0;
  if (c2<0) return 0;
  if (c3<0) return 0;
  if (c1==0 && c2==0 && c3==0) return 0;
  auto t = make_tuple(sum, c1, c2, c3);
  if (!memo[p].count(t)) {
    int ans=0;
    if (c1 > 0) ans = max(ans, dp(p, (sum+1)%p, c1-1, c2, c3));
    if (c2 > 0) ans = max(ans, dp(p, (sum+2)%p, c1, c2-1, c3));
    if (c3 > 0) ans = max(ans, dp(p, (sum+3)%p, c1, c2, c3-1));
    ans += (sum==0);
    memo[p][t] = ans;
  }
  return memo[p][t];
}

int solve() {
  int n, p; cin >> n >> p;
  array<int, 4> cnt={};
  for (auto _ : irange(int(0), n)) {
    (void)_;
    int x; cin >> x;
    ++cnt[x%p];
  }
  return cnt[0] + dp(p, 0, cnt[1], cnt[2], cnt[3]);
}

int main() {
  int testcases; cin >> testcases;
  for (auto i : irange(int(1), testcases+1)) {;
    cout << "Case #" << i << ": ";
    auto res = solve();
    if (res == -1) cout << "IMPOSSIBLE";
    else cout << res;
    cout << '\n';
  }
}

/*
 * Local variables:
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g3 -ggdb3 -O0 -Wall -Wextra -std=c++14 a.cc -o a && for f in *.in; do echo \"--- $f -------------\"; ./a <$f; done"
 * end:
 */

