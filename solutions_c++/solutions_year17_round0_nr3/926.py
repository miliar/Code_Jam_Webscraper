#include <bits/stdc++.h>
#include <string.h>
#define MAXN 50
#define ll long long int
#define mp make_pair
#define f first
#define s second

using namespace std;

ll n;

pair<ll,ll> lrF(ll k, ll l, ll r) {
	if(k == 1) return mp(l,r);
	if(k % 2 == 1) return lrF(k/2, (l-1)/2, l/2);
	return lrF((k+1)/2, (r-1)/2, r/2);
}

int main(void) {
	ll t;
	
	scanf("%I64d", &t);

	ll k;
	pair<ll,ll> ans;
	for(ll test = 1; test <= t; test++) {
		scanf("%I64d %I64d", &n, &k);
		ans = lrF(k, (n-1)/2, n/2);
		printf("Case #%I64d: %I64d %I64d\n", test, ans.s, ans.f);
	}
	
	
	return 0;
}