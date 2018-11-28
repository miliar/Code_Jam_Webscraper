#include "bits/stdc++.h"
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

#define FOR(i, s, e) for (ll(i) = (s); (i) < (e); (i)++)
#define FORR(i, s, e) for (ll(i) = (s); (i) > (e); (i)--)
#define debug(x) cout << #x << ": " << x << endl
#define mp make_pair
#define pb push_back
const ll MOD = 1000000007;
const int INF = 1e9;
const ll LINF = 1e16;
const double PI = acos(-1.0);
int dx[8] = {0, 0, 1, -1, 1, 1, -1, -1};
int dy[8] = {1, -1, 0, 0, 1, -1, 1, -1};

/* -----  xtimex  Problem:  / Link:   ----- */
/* ------問題------



-----問題ここまで----- */
/* -----解説等-----



----解説ここまで---- */

ll N;


void solve(int x) {
	string s; ll ans;
	cin >> s;
	s = '0' + s;
	FORR(i, s.size() - 1, 0) {
		if (s[i - 1] > s[i]) {
			int a = s[i - 1] - '0';
			FOR(j, i, s.size())s[j] = '9';
		 s[i - 1] = a - 1 + '0';
		}
	}
	ans = stoll(s);

	cout << "Case #" << x + 1 << ": " << ans << endl;
}

int main() {
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  cin >> N;
  FOR(i, 0, N) {
	  solve(i);
  }

  return 0;
}
