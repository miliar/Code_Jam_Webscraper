#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;

pair<ull, ull> solve(ull n, ull k) {
  if (k == 0) {
    if (n % 2) {
      return make_pair(n/2, n/2);
    } else {
      return make_pair(n/2, (n-1)/2);
    }
  } else {
    if (n % 2) {
      return solve(n/2, (k - 1)/2);
    } else {
      if (k % 2) {
        return solve(n/2, (k - 1)/2);
      } else {
        return solve((n - 1)/2, (k - 1)/2);
      }
    }
  }
}

int main() {
  int T;
  cin >> T;

  for (int tc = 1; tc <= T; tc++) {
    ull n, k;
    cin >> n >> k;
    auto ans = solve(n, k-1);
    cout << "Case #" << tc << ": " << ans.first << " " << ans.second << "\n";
  }

  return 0;
}
