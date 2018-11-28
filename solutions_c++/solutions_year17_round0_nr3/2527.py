#include <bits/stdc++.h>
using namespace std;
typedef long long Long;

void Solve(Long n, Long k) {
  n -= k;

  Long curr_x = 1;

  while (k - curr_x > 0) {
    k -= curr_x;
    curr_x *= 2;
  }

  curr_x *= 2;

  Long mn = n / curr_x;
  Long mx = mn;

  if (n % curr_x >= curr_x / 2) {
    ++mx;
  }

  cout << mx << ' ' << mn << '\n';
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif

  int t;
  cin >> t;

  for (int cs = 1; cs <= t; ++cs) {
    cout << "Case #" << cs << ": ";
    Long n, k;

    cin >> n >> k;
    Solve(n, k);
  }
}

