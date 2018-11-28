#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<ld, ld>
#define all(x) (x).begin(), (x).end()
#define fi first
#define se second

int Read() {
  string s;
  cin >> s;

  int x = 0;
  for (auto it : s) {
    if (it >= '0' && it <= '9') {
      x = x * 10 + it - '0';
    }
  }

  return x;
}

int main() {
  cin.sync_with_stdio(false);

  int t;
  cin >> t;
  for (int T = 1; T <= t; T++) {
    int n, k;
    cin >> n >> k;
    int to_spend = Read();

    multiset<int> s;
    for (int i = 1; i <= n; i++) {
      int p = Read();
      s.insert(p);
    }

    for (; to_spend; to_spend--) {
      int x = *s.begin();
      x++;
      s.erase(s.begin());
      s.insert(x);
    }

    double ans = 1.0;
    for (auto it : s) {
      ans = ans * 1.0 * it / 10000.0;
    }

    cout << "Case #" << T << ": ";
    cout << fixed << setprecision(9) << ans << '\n';
  }

  return 0;
}
