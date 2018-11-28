#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <vector>
#include <map>

using namespace std;
typedef long long ll;

ll N, K;
map<ll, ll> Mp;
vector<ll> List;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC; scanf("%d", &TC);
	for(int t=1; t<=TC; t++) {
		scanf("%lld%lld", &N, &K);
		Mp.clear(); List.clear();
		Mp[N] = 0; List.push_back(N);
		for(int i=0; i < List.size(); i++) {
			ll val = List[i];
			if(val == 0) continue; val--;
			for(ll x : vector<ll>({val/2, val-val/2}))
				if(Mp.count(x) == 0) {
					List.push_back(x);
					Mp[x] = 0;
				}
		}
		sort(List.begin(), List.end(), [&](const ll &a, const ll &b) {return a > b;});
		Mp[N] = 1;
		ll minV = -1, maxV = -1;
		for(int i=0; i<List.size(); i++) {
			ll val = List[i], now = Mp[val];
			if(K > now) {
				val--;
				Mp[val/2] += now;
				Mp[val-val/2] += now;
				K -= now;
			} else {
				val--;
				minV = val / 2;
				maxV = val - val/2;
				break;
			}
		}
		
		printf("Case #%d: %lld %lld\n", t, maxV, minV);
	}
	return 0;
}