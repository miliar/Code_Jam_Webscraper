#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int t;
ll n, k;

map<ll,ll> mem;

ll f(ll n, ll d) {
	if(mem.find(n)!=mem.end()) return mem[n];
	if(n<d) return 0;
	return mem[n]=1+f((n-1)/2, d)+f(n-1-(n-1)/2, d);
}

ll bin(ll n, ll k) {
	ll l=0, r=n;
	while(l<r) {
		ll mi=(l+r+1)/2;
		mem.clear();
		if(f(n, mi)>=k) l=mi;
		else r=mi-1;
	}
	return l;
}

int main()
{
scanf("%d", &t);
for(int q=1; q<=t; q++) {
	scanf("%lld%lld", &n, &k);
	ll len=bin(n, k);
	printf("Case #%d: %lld %lld\n", q, len-1-(len-1)/2, (len-1)/2);
}

	return 0;
}
