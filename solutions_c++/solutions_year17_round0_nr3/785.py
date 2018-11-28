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

map <ll, ll> qtd;
void solve (ll x) {
	if (x%2) cout << x/2 << " " << x/2 << endl;
	else cout << x/2 << " " << x/2-1 << endl;
}
int main (void) {
	int t; scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++) {
		ll n, k;
		scanf("%lld %lld", &n, &k);
		qtd[n] = 1;
		vector <ll> v;
		v.pb(n);
		while (true) {
			set <ll> novo;
			for (auto e : v) {
				if (e%2==0) novo.insert(e/2);
				if (e%2==0) novo.insert(e/2 - 1);
				else novo.insert(e/2);
			}
			novo.erase(0);
			v.clear();
			for (auto e : novo) {
				qtd[e] = qtd[e*2 + 1] * 2;
				if (e%2) {
					qtd[e] += qtd[e*2];
					qtd[e] += qtd[e*2+2];
				} else {
					qtd[e] += qtd[e*2+2];
					qtd[e] += qtd[e*2];
				}
				v.pb(e);
			}
			if (novo.empty()) break;
		}	
		qtd[0] = 0;
		ll ans = 0;
		printf("Case #%d: ", cases);
		for (map<ll,ll>::reverse_iterator it = qtd.rbegin(); it != qtd.rend(); it++) {
			ans += it->se;
			if (ans >= k) {
				solve (it->fi);
				break;
			}
		}
		qtd.clear();
	}
	return 0;
}
