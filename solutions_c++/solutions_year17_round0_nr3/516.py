#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
typedef pair<ll, ll> ii;
int main(){
	map<ll, ll> tree;
	int cases; cin >> cases;
	for(int cs = 1; cs <= cases; cs++){
		ll n, k; cin >> n >> k;
		tree.clear();
		tree[n] = 1;
		cout << "Case #" << cs << ": ";
		while(k > 0){
			auto it = tree.end(); it--;
			ll sz = it->first;
			ll cnt = it->second;
			//cout << sz << endl;
			if(cnt >= k) break;
			k -= cnt;
			tree.erase(it);
			tree[sz/2] += cnt;
			tree[max(0ll, sz/2 - (1 - sz%2))] += cnt;
		}
		auto it = tree.end(); it--;
		ll sz = it->first;
		cout << sz/2 << " " << max(0ll, (sz/2 - (1 - sz%2))) << endl;
	}
	return 0;
}

