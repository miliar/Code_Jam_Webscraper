#include <bits/stdc++.h>

#define eb emplace_back
#define pb push_back
#define fi first
#define se second
#define mp make_pair
#define INF 0x3f3f3f3f

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
const int N = 100010;

ll dp[20][11][2][2];
string s;
ll solve (int pos, int last, int menor, int leading) {
	if (pos == -1) return !leading;
	ll &ret = dp[pos][last][menor][leading];
	if (ret != -1) return ret;
	ret = 0;
	if (menor) {
		for (int i = last; i <= 9; i++) {
			ret += solve (pos-1, i, menor, i ? 0 : leading);
		}
	} else {
		if (last <= s[pos]-'0') ret = solve (pos-1, s[pos]-'0', 0, s[pos] == '0' ? leading : 0);
		for (int i = last; i < s[pos] - '0'; i++) {
			ret += solve (pos-1, i, 1, i ? 0 : leading);
		}
	}
	return ret;
}
void converte (ll x) {
	memset (dp, -1, sizeof dp);
	s.clear();
	while (x) {
		s.pb(x%10 + '0');
		x /= 10;
	}
}
int main (void) {
	int t; scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++) {
		ll n; cin >> n;
		converte(n);
		ll qtd = solve (s.size()-1, 0, 0, 1);
		ll lo = 1, hi = n, ans = 0;
		while (lo <= hi) {
			ll mid = (lo + hi) / 2;
			converte (mid);
			ll qtd2 = solve (s.size()-1, 0, 0, 1);
			if (qtd2 < qtd) {
				lo = mid+1;
			} else if (qtd2 == qtd) {
				ans = mid;
				hi = mid-1;
			} else hi = mid-1;
		}
		printf("Case #%d: ", cases);
		cout << ans << endl;
	}
	return 0;
}
