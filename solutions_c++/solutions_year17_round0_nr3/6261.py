#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> pi;



int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1;  t <= T; t++) {
    ll n, k;
    cin >> n >> k;
    set<pi> ba;
    ba.insert({-n, 0});
    ll ls, rs;
    for (int i = 0; i < k; i++) {
      pi  z = *ba.begin();
      ba.erase(ba.begin());
      ll x = -z.first;
      x--;
      ll y = z.second;
      ba.insert({-(x/2), y}); 
      ba.insert({-(x-x/2), y + 1 + x/2});
      rs = x-x/2;
      ls = x/2;
    }

    cout << "Case #" << t << ": " << max(rs, ls) << " " << min(rs, ls) << "\n";  
  }
  return 0;
}
