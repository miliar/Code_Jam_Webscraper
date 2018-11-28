#include <bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)
#define REP(i,a) FOR(i,0,(int)(a)-1)
#define reset(a,b) memset(a,b,sizeof(a))
#define BUG(x) cout << #x << " = " << x << endl
#define PR(x,a,b) {cout << #x << " = "; FOR (_,a,b) cout << x[_] << ' '; cout << endl;}
#define CON(x) {cout << #x << " = "; for(auto i:x) cout << i << ' '; cout << endl;}
#define mod 1000000007
#define pi acos(-1)
#define eps 0.00000001
#define pb push_back
#define sqr(x) (x) * (x)
#define _1 first
#define _2 second

int t, k;
string s;

int main() {
  ios::sync_with_stdio(false);
  cin >> t;
  FOR (cas, 1, t) {
  	cout << "Case #" << cas << ": ";
  	cin >> s >> k;
  	int ans = 0;
  	for (int i = 0; i + k <= s.size(); i++) if (s[i] == '-') {
  		ans++;
  		REP (j, k) s[i + j] = '-' + '+' - s[i + j];
  	}
  	bool flag = false;
  	for (char c: s) if (c == '-') flag = true;
  	if (flag) cout << "IMPOSSIBLE" << endl;
  	else cout << ans << endl;
  }
}
