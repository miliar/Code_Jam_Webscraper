#include <bits/stdc++.h>

#define all(x) x.begin(),x.end()
using namespace std;

typedef long long ll;
typedef long double ld;

int run() {
  ll t;
  cin >> t;
  for (int q = 0; q < t; ++q) {
    ll n;
    ll r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    string ans;
    ans.assign(n, '-');
    ll cur = 0;
    vector<pair<ll, char>> vec;
    vec.push_back({r, 'R'});
    vec.push_back({y, 'Y'});
    vec.push_back({b, 'B'});
    sort(vec.rbegin(), vec.rend());
    for (auto i : vec) {
      for (int j = 0; j < i.first; j++) {
        ans[cur] = i.second;
        cur += 2;
        if (cur >= n) cur = 1;
      }
    }
    bool isimp = false;
    for (int i = 0; i < n - 1; ++i) {
      if (ans[i] == ans[i + 1]) isimp = true;
    }
    if (ans[0] == ans[n - 1]) isimp = true;
    cout << "Case #" << q + 1 << ": ";
    if (isimp) cout << "IMPOSSIBLE\n";
    else cout << ans << endl;
  }
}


int main() {
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  run();
  return 0;
}