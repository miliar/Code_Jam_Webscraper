#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<ll> VL;
typedef vector<VL> VVL;
typedef pair<int, int> PII;

#define FOR(i, a, n) for (ll i = (ll)a; i < (ll)n; ++i)
#define REP(i, n) FOR(i, 0, n)
#define ALL(x) x.begin(), x.end()
#define MP make_pair
#define PB push_back
#define MOD 1000000007
#define INF (1LL<<30)
#define LLINF (1LL<<60)
#define PI 3.14159265359
#define EPS 1e-12
#define int ll

int s[105];
signed main(void)
{
  int t;
  cin >> t;
  REP(i, t) cin >> s[i];

  REP(i, t) {
    if(s[i] < 10) {
      cout << "Case #" << i+1 << ": " << s[i] << endl;
      continue;
    }
    for(int j=s[i]; j>=9; --j) {
      string t = to_string(j);
      bool flag = true;
      FOR(k, 1, t.size()) {
        if(t[k] < t[k-1]) flag = false;
      }
      if(flag) {
        cout << "Case #" << i+1 << ": " << j << endl;
        break;
      }
    }
  }

  return 0;
}
