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

string s[105];
signed main(void)
{
  int t, a[105];
  cin >> t;
  REP(i, t) cin >> s[i] >> a[i];

  REP(i, t) {
    int ret = 0;
    for(int j=s[i].size()-1; j>=a[i]-1; --j) {
      if(s[i][j] == '-') {
        for(int k=j; k>j-a[i]; --k) {
          //cout << k << " ";
          if(s[i][k] == '+') s[i][k] = '-';
          else s[i][k] = '+';
        }
        //cout << endl;
        ret++;
      }
    }
    bool flag = true;
    REP(j, s[i].size()) if(s[i][j] == '-') flag = false;
    if(flag) cout << "Case #" << i+1 << ": " << ret << endl;
    else cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
  }

  return 0;
}
