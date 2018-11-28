#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define DEBUG
#ifdef DEBUG
#define TRACE(x) cerr << #x << " = " << x << endl;
#define _ << " _ " <<
#else
#define TRACE(x) ((void)0)
#endif

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cout << "Case #" << tt << ": ";
    ll n, k;
    cin >> n >> k;
    map<ll, ll> cnts;
    cnts[n] = 1;
    while (k > 0) {
      ll key, val;
      tie(key, val) = *cnts.rbegin();
      if (val >= k) {
        cout << key / 2 << ' ' << (key - 1) / 2;
        break;
      } else {
        k -= val;
        cnts[key / 2] += val;
        cnts[(key - 1) / 2] += val;
        cnts.erase(--cnts.end());
      }
    }
    cout << '\n';
  }

  return 0;
}
