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

map<ll, ll, greater<ll>> m;

int main() {
  cin.sync_with_stdio(false);

  int t;
  cin >> t;
  for (int test = 1; test <= t; test++) {
    ll n, k;
    cin >> n >> k;

    m.clear();
    m[n] = 1;

    cout << "Case #" << test << ": ";
    while (1) {
      ll val = m.begin()->first;
      ll cnt = m.begin()->second;

      k -= cnt;
      ll a = val / 2;
      ll b = (val - 1) / 2;

      if (k <= 0) {
        cout << a << " " << b << '\n';
        break;
      }

      m[a] += cnt;
      m[b] += cnt;
      m.erase(m.begin());
    }
  }

  return 0;
}
