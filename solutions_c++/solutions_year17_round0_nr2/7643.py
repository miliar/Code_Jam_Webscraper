#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

bool tidy(ll n) {
  int nou, prev = 10;
  while (n) {
    nou = n%10;
    n /= 10;
    if (nou > prev) return false;
    prev = nou;
  }
  return true;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1;  t <= T; t++) {
    ll n, res; 
    cin >> n;
    for (ll i = n; i >= 0; i--)
      if (tidy(i)) {
        res = i; 
        break;
      }
    cout << "Case #" << t << ": " << res << endl;  
  }
  return 0;
}
