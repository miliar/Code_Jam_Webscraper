#include <bits/stdc++.h>
using namespace std;
#define ll long long
int T;
ll n, k, cnt;
pair<ll, ll>p;
map<ll, ll>m;
ll dfs(ll x) {
	if (m.find(x)!=m.end()) return m[x];
	ll r=(x/2), l=(x-1)/2, sum=0;
	if (r>=p.first&&l>=p.second) sum++;
	if (l+r==0) return sum;
	sum+=dfs(l)+dfs(r);
	return m[x]=sum;
}
bool check() {
	m.clear();
	if (dfs(n)>=k) return true;
	return false;
}
void solve(int test) {
	scanf("%lld %lld", &n, &k);
	ll lo=0, hi=n;
	while (lo+1<hi) {
		ll mid=(lo+hi)/2;
		p={mid/2, mid/2};
		if (mid%2) p.first++;
		//printf("%lld %lld\n", p.first, p.second);
		if (check()) lo=mid;
		else hi=mid;
	}
	p={lo/2, lo/2};
	if (lo%2) p.first++;
	printf("Case #%d: %lld %lld\n", test, p.first, p.second);
}
int main () {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &T);
	for (int i=1; i<=T; i++) {
		solve(i);
	}
	return 0;
}
