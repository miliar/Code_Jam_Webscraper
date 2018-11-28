#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
	
	int T;
	scanf("%d", &T);
	
	for(int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		
		ll N, K;
		scanf("%lld %lld", &N, &K);
		
		map<ll, ll> mm;
		mm[N] = 1;
		
		while(true) {
			pair<ll,ll> it = *(mm.rbegin());
			if(K <= it.second) {
				printf("%lld %lld\n", it.first/2, (it.first-1)/2);
				break;
			}
			K -= it.second;
			if(it.first&1LL) {
				ll size = it.first/2;
				ll count = 2*it.second;
				if(mm.find(size) != mm.end()) {
					mm[size] += count;
				} else {
					mm[size] = count;
				}
			} else {
				ll size1 = it.first/2;
				ll size2 = (it.first-1)/2;
				ll count = it.second;
				if(mm.find(size1) != mm.end()) {
					mm[size1] += count;
				} else {
					mm[size1] = count;
				}
				if(mm.find(size2) != mm.end()) {
					mm[size2] += count;
				} else {
					mm[size2] = count;
				}
			}
			mm.erase(it.first);
		}
	}
	
	return 0;
}
