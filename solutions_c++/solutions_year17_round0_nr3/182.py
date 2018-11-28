#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

typedef long long ll;

ll c0(ll x) { return x/2; }
ll c1(ll x) { return x-x/2; }

ll sim(ll v1, ll n1, ll v2, ll n2, ll k) {
	if(k<=n1) return v1;
	if(k<=n1+n2) return v2;
	if(v1==v2) {
		if((v1&1)==0) return sim(c0(v1), 2*n1, c0(v1), 0, k-n1-n2);
		else return sim(c1(v1), n1, c0(v1), n1, k-n1-n2);
	}
	else {
		if((v1&1)==0) return sim(c1(v1), 2*n1+n2, c0(v2), n2, k-n1-n2);
		else return sim(c1(v1), n1, c0(v1), n1+2*n2, k-n1-n2);
	}
}

int main() {
	int ncase, icase;
	ll x, k, ans;
	scanf("%d", &ncase);
	for(icase=1; icase<=ncase; icase++) {
		scanf("%lld%lld", &x, &k);
		ans=sim(x+1, 1, x+1, 0, k);
		printf("Case #%d: %lld %lld\n", icase, c1(ans)-1, c0(ans)-1);
	}
	return 0;
}