#include <bits/stdc++.h>
using namespace std;
using ll =long long;
using vl=vector<ll>;
using vs=vector<string>;
using vvl=vector<vl>;
using pll=pair<ll,ll>;
const ll oo =0x3f3f3f3f3f3f3f3fLL;
const double eps=1e-9;
#define sz(c) ll((c).size())
#define all(c) begin(c),end(c)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define xx first
#define yy second
#define FOR(i,a,b) for(ll i=(a); i<(b); i++)
#define FORD(i,a,b) for(ll i=ll(b)-1;i>=(a);i--)
#define TR(X) ({if(1) cerr << "TR: " << (#X) << " = " << (X) << endl; })
int main(){ cin.sync_with_stdio(0);
	ll T; cin >> T;
	FOR(TC, 1, T+1) {
		ll N, K; cin >> N >> K;

		map<ll, ll> segs;
		segs[N] = 1;

		ll res = -1;
		while (K > 0) {
			pll cur = *prev(segs.end());
			segs.erase(prev(segs.end()));
			
			K -= cur.yy;
			res = cur.xx;

			if (res % 2 == 0) {
				segs[res/2] += cur.yy;
				segs[res/2 - 1] += cur.yy;
			} else {
				segs[res/2] += cur.yy * 2;
			}
		}
		ll left, right;
		if (res % 2 == 0) {
			left = res/2 - 1;
			right = res/2;
		} else {
			left = res/2;
			right = res/2;
		}
		cout << "Case #" << TC << ": " << max(left, right) << " " << min(left, right) << endl;
	}
} //cin.tie(0) bei schnellem Wechseln
