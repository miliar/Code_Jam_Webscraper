#include <bits/stdc++.h>
using namespace std;
#define ll long long
int T, n, k;
double u, a[100];
void solve(int test) {
	scanf("%d %d", &n, &k);
	printf("Case #%d: ", test);
	scanf("%lf", &u);
	for (int i=0; i<n; i++) scanf("%lf", &a[i]);
	double lo=0, hi=1;
	for (int t=0; t<100; t++) {
		double mid=(lo+hi)/2.0, s=u;
		for (int i=0; i<n; i++) {
			if (a[i]>=mid+1e-9) continue;
			s-=mid-a[i];
		}
		if (s>=0) lo=mid;
		else hi=mid;
	}
	double ans=1;
	for (int i=0; i<n; i++) {
		if (a[i]>=lo+1e-9) ans*=a[i];
		else ans*=lo;
	}
	printf("%.10lf\n", ans);
}
int main () {
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	scanf("%d", &T);
	for (int i=1; i<=T; i++) {
		solve(i);
	}
	return 0;
}
