#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iterator>

typedef long long ll;

using namespace std;

int main() {
  freopen("in.in", "r", stdin);
  freopen("in2.out", "w", stdout);
  ios::sync_with_stdio(false);
  cin.tie(0);

  int t;
  cin >> t;

  for (int tt = 1; tt <= t; tt++) {
    ll n, k;
    cin >> n >> k;
    map<ll, ll> ma;
    ma[n] = 1;
    cout << "Case #" << tt << ": ";
    bool keep = true;
    while(keep) {
      map<ll, ll> next;
      map<ll, ll>::reverse_iterator it;
      for(it = ma.rbegin(); it != ma.rend(); it++) {
        ll x = it->first - 1;
        ll y = it->second;
        if (y >= k) {
          cout << x / 2 + (x % 2) << " " << x /2 << endl;
          keep = false;
          break;
        }
        k -= y;
        if (x % 2) {
          next[x / 2] += y;
          next[x / 2 + 1] += y;
        } else {
          next[x / 2] += y * 2;
        }
      }
      ma = next;
    }
  }



  return 0;
}
