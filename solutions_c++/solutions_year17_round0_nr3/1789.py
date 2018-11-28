#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
map<ll, ll> dt;
priority_queue<ll> pq;

void solve (ll tc) {
	ll n, k;
	scanf("%lld%lld",&n,&k);
	dt[n] = 1;
	pq.push(n);
	while(!pq.empty()) {
		ll cur = pq.top(); pq.pop();
		ll tmp = dt[cur];
		if(tmp >= k) {
			while(!pq.empty()) pq.pop();
			printf("Case #%lld: %lld %lld\n", tc, cur/2, (cur-1)/2);
			break;
		}
		else {
			k -= tmp;
			if(dt[cur/2] == 0) pq.push(cur/2);
			dt[cur/2] += tmp;
			if(dt[(cur-1)/2] == 0) pq.push((cur-1)/2);
			dt[(cur-1)/2] += tmp;
		}
	}
	dt.clear();
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ll tc;
	scanf("%lld",&tc);
	for(ll i=1;i<=tc;i++) solve(i);
}
