#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

const ll MAXN = 50 + 3;

ll n, m, a[MAXN][MAXN], pt[MAXN], req[MAXN];

bool ok(ll mn, ll i, ll x){
	ll nd = 1ll*mn*req[i];
	if (10ll*x < 9ll*nd) return false;
	if (10ll*x > 11ll*nd) return false;
	return true;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	ll te;	cin >> te;
	for (ll w = 1; w <= te; w++){
		ll ans = 0;
		memset(pt, 0, sizeof(pt));
		cin >> n >> m;
		for (ll i = 0; i < n; i++)	cin >> req[i];
		for (ll i = 0; i < n; i++){
			for (ll j = 0; j < m; j++)	cin >> a[i][j];
			sort(a[i], a[i] + m);
		}

		while (1){
			bool done = 0;
			for (ll i = 0; i < n; i++)
				if (pt[i] == m) done = 1;
	
			if (done) break;
			ll mn = 1e9;
			for (ll i = 0; i < n; i++)
				mn = min(mn, 10*a[i][pt[i]]/(9*req[i]));

			bool fail = 0;
			for (ll i = 0; i < n; i++)
				if (!ok(mn, i, a[i][pt[i]])){
					fail = 1;
					break;
				}

			if (fail){
				for (ll i = 0; i < n; i++)
					if (mn == 10*a[i][pt[i]]/ (9*req[i])){
						pt[i]++;
						break;
					}
			}
			else{
				ans++;
				for (ll i = 0; i < n; i++) pt[i]++;
			}
		}

		cout << "Case #" << w << ": " << ans << "\n";
	}
	return 0;
}
