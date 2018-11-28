#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>

using namespace std;
typedef long long ll;

map<ll, ll> m;

int main(){

	int t;
	scanf("%d\n", &t);
	
	ll n, k;
	int caso = 1;
	while(t--){
		scanf("%lld %lld", &n, &k);	
		m[n] = 1;
		ll ans;
		while(k > 0){
			ll a = (prev(m.end()))->first;
			
			ll b = (prev(m.end()))->second;
			ll tmp = a>>1;
			if(a&1){
				m[tmp] += 2LL*b;
			}else{
				m[tmp] += b;
				m[tmp-1] += b;
			}
			ans = a;
			k -= b;
			m.erase(a);
		}

		printf("Case #%d: %lld %lld\n",caso, ans>>1, (ans-1) >>1);
		caso++;
		m.clear();
	}


	return 0;
}