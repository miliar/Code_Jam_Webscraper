#include<bits/stdc++.h>
#define rep(i,n)for(int i=0;i<(n);i++)
using namespace std;

double k[1000], s[1000];
int main() {
	int T; scanf("%d", &T);
	for (int CASE = 1; CASE <= T; CASE++) {
		int d, n; scanf("%d%d", &d, &n);
		rep(i, n)scanf("%lf%lf", &k[i], &s[i]);
		double Min = LLONG_MAX;
		rep(i, n) {
			Min = min(Min, d / ((d - k[i]) / s[i]));
		}
		printf("Case #%d: %.12lf\n", CASE, Min);
	}
}