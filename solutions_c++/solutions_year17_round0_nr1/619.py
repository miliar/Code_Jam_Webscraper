#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ll> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define INF 1e9
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

int countFlips(vi &flips, int index) {
  return flips.size() - (upper_bound(flips.begin(), flips.end(), index) - flips.begin());
}

int main() {
  ios::sync_with_stdio(false);
  int t, l, k, f, s, r;
  char pancakes[1002];
  cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    cin >> pancakes >> k;
    l = strlen(pancakes);
    r = 0;
    vi flips;
    for (int i = 0; i <= l - k; i++) {
      f = countFlips(flips, i);
      s = ((pancakes[i] == '-') + f)%2;
      if (s) {
        r++;
        flips.pb(i + k);
      }
    }
    for (int i = l - k + 1; i < l; i++) {
      f = countFlips(flips, i);
      s = ((pancakes[i] == '-') + f)%2;
      if (s) {
        r = -1;
        break;
      }
    }
    cout << "Case #" << tc << ": ";
    if (r == -1) cout << "IMPOSSIBLE" << endl;
    else cout << r << endl;
  }
}
