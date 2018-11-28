#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

int main() {
		freopen("B-large.in", "r", stdin);
		freopen("Csmallest.txt", "w", stdout);

	int t, tc = 1; cin >> t;
	while(t--){
		ll n, k; cin >> n >> k;
		map<ll, ll>cnt;
		cnt[n] = 1;
		ll mn, mx;
		for(map<ll, ll>::reverse_iterator it = cnt.rbegin(); it != cnt.rend(); it++){
			if(k <= it->second){
				mx = it->first / 2;
				mn = (it->first - 1) / 2;
				break;
			}

			k -= it->second;
			cnt[it->first / 2] += it->second;
			cnt[(it->first - 1) / 2] += it->second;
		}

		cout << "Case #" << tc++ << ": " << mx << ' ' << mn << endl;
	}

	return 0;
}
