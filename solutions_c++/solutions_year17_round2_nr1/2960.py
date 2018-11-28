#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;

int main(){
	freopen("A-large (1).in", "r", stdin);
	freopen("aaaa", "w", stdout);
	int T; cin >> T;
	for (int t = 1; t <= T; t++){
		int n;
		double d;
		scanf("%lf%d", &d, &n);
		double mx = DBL_MIN;
		for (int i = 0; i < n; i++){
			double x, y;
			scanf("%lf%lf", &x, &y);
			mx = max(mx, (d - x) / y);
		}
		printf("Case #%d: %0.6lf\n", t, d / mx);
	}
	return 0;
}