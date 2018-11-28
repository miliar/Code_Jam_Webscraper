#include <bits/stdc++.h>
using namespace std;
int T;
#define ll long long
ll d, n, x, y;
void solve(int test) {
	scanf("%lld %lld", &d, &n);
	double ans=0;
	while (n--) {
		scanf("%lld %lld", &x, &y);
		ans=max(ans, 1.0*(d-x)/y);
	}
	ans=1.0*d/ans;
	printf("Case #%d: %.10lf\n", test, ans);
	
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
