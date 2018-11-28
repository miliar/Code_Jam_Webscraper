#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define F first
#define S second

pair<ll, ll> f(ll n, ll k){
	ll mid = (1 + n) >> 1;
	ll left = mid - 1, right = n - mid;
	if(k == 1) return {left, right};
	k --;
	ll khalf = k >> 1;
	if(n & 1){
		// start from left.
		if(k & 1) return f(left, k - khalf);
		return f(right, khalf);
	}
	// start from right
	if(k & 1) return f(right, k - khalf);
	return f(left, khalf);
}
int main(){
	int t;
	scanf("%d", &t);
	ll n, k;
	for(int tt = 1; tt <= t; tt++){
		// cerr << tt << endl;
		scanf("%lld %lld", &n, &k);
		// cerr << n << " " << k << endl;
		pair<ll, ll> P = f(n, k);
		printf("Case #%d: %lld %lld\n", tt, P.S, P.F);
	}
}