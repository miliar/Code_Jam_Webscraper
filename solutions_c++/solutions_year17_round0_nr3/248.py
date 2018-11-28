#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
typedef long long ll;

int main(){
	int T; scanf("%d", &T);
	for(int ti=1;ti<=T;ti++){
		fprintf(stderr, "start test case %d\n", ti);
		ll n, k; scanf("%lld%lld", &n, &k);
		map<ll, ll> m;
		m[n]++;
		ll ans_sz;
		while(true){
			auto it = m.end(); it--;
			ll val = it->first;
			ll num = it->second;
			m.erase(it);
			if(k <= num){
				ans_sz = val;
				break;
			}
			k -= num;
			ll a = (val - 1) / 2;
			ll b = val - 1 - (val - 1) / 2;
			if(a != 0) m[a] += num;
			if(b != 0) m[b] += num;
		}
		ll a = (ans_sz - 1) / 2;
		ll b = ans_sz - 1 - (ans_sz - 1) / 2;
		printf("Case #%d: %lld %lld\n", ti, max(a, b), min(a, b));
	}
	return 0;
}
