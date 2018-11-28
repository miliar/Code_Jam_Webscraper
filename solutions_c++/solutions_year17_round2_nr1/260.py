#include <bits/stdc++.h>
using namespace std;

#define int int_fast64_t

double solve() {
  double ans = numeric_limits<double>::max();
  auto cap = [&](double d) {
    if (d < ans)
      ans = d;
  };
  
  int d, n; cin >> d >> n;
  while (n--) {
    int k, s; cin >> k >> s;
    cap(d*(double)s/(double)(d-k));
  }
  return ans;
}

signed main() {
  ios_base::sync_with_stdio(false), cin.tie(nullptr);

  int n; cin >> n;
  for (int i=1; i<=n; ++i) {
    cout << setprecision(100) << "Case #" << i << ": " << solve() << '\n';
  }
}

/*
 * Local variables:
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g3 -ggdb3 -O0 -Wall -Wextra -std=c++14 a.cc -o a && for f in *.in; do echo \"--- $f -------------\"; ./a <$f; done"
 * end:
 */

