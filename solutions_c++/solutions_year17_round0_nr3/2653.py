#include "bits/stdc++.h"
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<pll, ll> plll;

#define FOR(i, s, e) for (ll(i) = (s); (i) < (e); (i)++)
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


pll solve() {
	ll ans1, ans2;
	ll N, K; cin >> N >> K;
	//if (N < 2*K)return mp(0, 0);
	vector<plll>v1;
	vector<plll>v2;
	// [(a,b),c] すでに一つ置いたときに左にa,右にｂこ空があるという状態
	v1.push_back(mp(mp(N - (N - 1) / 2 - 1, (N - 1) / 2), 1));
	ll k = 0;
	for (;;) {

		//FOR(i, 0, v1.size()) {
		//	ll s1 = v1[i].first.first;
		//	ll s2 = v1[i].first.second;
		//	ll num = v1[i].second;
		//	cout << "v1 " << i << " k: " << k << " s1: " << s1 << " s2: " << s2 << " num:" << num << endl;
		//}
		FOR(i, 0, v1.size()) {
			ll s1 = v1[i].first.first;
			ll s2 = v1[i].first.second;
			ll num = v1[i].second;
			//cout << "k: " << k << " s1: " << s1 << " s2: " << s2 << " num:" << num << endl;
			if (k + num >= K) {
				ans1 = s1; ans2 = s2;
				if (s2 > s1)swap(ans1, ans2);
				return mp(ans1, ans2);
			}
			else {
				if (s1 == 0 && s2 == 0);
				else if (s1 == 0 || s2 == 0) {
					v2.push_back(mp(mp(0, 0), num));
				}
				else if (s1 == s2)
					v2.push_back(mp(mp(s1 - (s1 - 1) / 2 - 1, (s1 - 1) / 2), 2 * num));
				else {
					v2.push_back(mp(mp(s1 - (s1 - 1) / 2 - 1, (s1 - 1) / 2), num));
					v2.push_back(mp(mp(s2 - (s2 - 1) / 2 - 1, (s2 - 1) / 2), num));
				}
			}
			k += (num);
		}

		/*cout << "sort" << endl;
		cout << "size1: " << v1.size() << " s2: " << v2.size() << endl;*/

		sort(v2.begin(), v2.end(), greater<plll>());
		v1.clear();
		//debug(v1.size());

		FOR(i, 0, v2.size()) {// v2 => v1
			if (i + 1 != v2.size()) {//末尾でない
				if (v2[i].first.first == v2[i + 1].first.first&&v2[i].first.second == v2[i + 1].first.second) {
					v2[i + 1].second = v2[i].second + v2[i + 1].second;
				}
				else v1.push_back(v2[i]);
			}
			else v1.push_back(v2[i]);
		}

		v2.clear();
		/*debug(v2.size());
		FOR(i, 0, v1.size()) {
			ll s1 = v1[i].first.first;
			ll s2 = v1[i].first.second;
			ll num = v1[i].second;
			cout << "v1 " << i << " k: " << k << " s1: " << s1 << " s2: " << s2 << " num:" << num << endl;
		}

		cout << "-----------------------------------------------" << endl;*/
	}
}


int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	FOR(i, 0, t) {
		pll a = solve();
		cout << "Case #" << i + 1 << ": " << a.first << " " << a.second << endl;

	}
	return 0;
}
