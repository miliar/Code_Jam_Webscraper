#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

map<ll, ll> m;

int main(void) {
	ios::sync_with_stdio(false);
	int T;	
	cin >> T;
	for(int t = 1; t <= T; t++) {
		m.clear();
		ll n, k;	
		cin >> n >> k;
		m[n] = 1;
		ll mn, mx;
		while(k) {
			auto it = m.end();
			it--;
			ll sz = it->fi;
			ll cnt = it->se;
			mn = (sz-1)/2;
			mx = (sz)/2;
			ll aux = min(k, cnt);
			m[mn] += aux;
			m[mx] += aux;
			m.erase(it);
			k -= aux;
		}
		cout << "Case #" << t << ": " << mx << " " << mn << endl;
	}
	
	return 0;
}
