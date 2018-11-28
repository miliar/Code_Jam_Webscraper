#include "bits/stdc++.h"
#include <string>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

#define FOR(i, s, e) for (int(i) = (s); (i) < (e); (i)++)
#define FORR(i, s, e) for (ll(i) = (s); (i) > (e); (i)--)
#define debug(x) cout << #x << ": " << x << endl
#define mp make_pair
#define pb push_back
const ll MOD = 1000000007;
const int INF = 1e9;
const ll LINF = 1e16;
const double PI = acos(-1.0);
int dx[8] = { 0, 0, 1, -1, 1, 1, -1, -1 };
int dy[8] = { 1, -1, 0, 0, 1, -1, 1, -1 };

/* -----  xtimex  Problem:  / Link:   ----- */
/* ------問題------



-----問題ここまで----- */
/* -----解説等-----



----解説ここまで---- */

ll N;


void solve(int x) {
	string S; int K; string ans = "IMPOSSIBLE";
	int cnt = 0;
	cin >> S >> K;
	FOR(i, 0, S.size() - K + 1) {
		if (S[i] == '-') {
			cnt++;
			FOR(j, 0, K) {
				if (S[i + j] == '-')S[i + j] = '+';
				else S[i + j] = '-';
			}
		}
		debug(S);
	}
	bool flag = true;
	FOR(i, 0, S.size()) {
		if (S[i] == '-')flag = false;
	}
	if (flag)
		cout << "Case #" << x + 1 << ": " << cnt << endl;
	else
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
