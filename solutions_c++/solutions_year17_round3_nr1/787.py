#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi 3.1415926535897932384626
int T, n, k;
ll r[1005], h[1005];
pair<ll, ll>a[1005];
void solve(int test) {
	scanf("%d %d", &n, &k);
	for (int i=0; i<n; i++) {
		scanf("%lld %lld", &r[i], &h[i]);
		a[i].first=2LL*r[i]*h[i];
		a[i].second=i;
	}
	sort(a, a+n);
	ll ans=0, sum=0;
	for (int i=0; i<n; i++) {
		sum=r[i]*r[i]+2LL*r[i]*h[i];
		int cnt=1;
		for (int j=n-1; j>=0; j--) {
			if (cnt==k) break;
			if (i==a[j].second) continue;
			sum+=a[j].first;
			cnt++;
		}
		ans=max(ans, sum);
	}
	printf("Case #%d: ", test);
	printf("%.10lf\n", 1.0*pi*ans);
}
int main () {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int i=1; i<=T; i++) {
		solve(i);
	}
	return 0;
}
