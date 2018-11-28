#include <bits/stdc++.h>
#define SZ(v) ((int)(v).size())

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<int, ll> pil;

struct col {
	bool one;
	ll a;
	ll b;
	ll cnta;
	ll cntb;
} c[103];

pil getans(ll k){
	if (k == 1) return {0, 1LL};
	auto subp = getans(k>>1);
	if (k&1){
		return {subp.first+1, 2*subp.second};
	}
	else return {subp.first+1, 2*subp.second-1};
}

int main(){
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++){
		ll n, k;
		scanf("%lld%lld", &n, &k);
		c[0] = {true, n, -1, 1, 0};
		for (int i=1; i<100; i++){
			if (c[i-1].b == 0) break;
			if (c[i-1].one){
				ll get = c[i-1].a;
				get--;
				if (get&1){
					c[i] = {false, get/2+1, get/2, c[i-1].cnta, c[i-1].cnta};
				}
				else {
					c[i] = {true, get/2, -1, c[i-1].cnta*2, 0};
				}
			}
			else {
				ll get = c[i-1].a;
				get--;
				if (get&1){
					c[i] = {false, get/2+1, get/2, c[i-1].cnta, c[i-1].cnta + 2*c[i-1].cntb};
				}
				else {
					c[i] = {false, get/2, get/2-1, c[i-1].cnta*2 + c[i-1].cntb, c[i-1].cntb};
				}
			}
		}
		auto ans = getans(k);
		ll node = c[ans.first].cnta >= ans.second ? c[ans.first].a : c[ans.first].b;
		node--;
		printf("Case #%d: ", t);
		if (node&1){
			printf("%lld %lld\n", node/2+1, node/2);
		}
		else printf("%lld %lld\n", node/2, node/2);
	}
	return 0;
}