#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;


void work() {
	double D;
	int n;
	scanf("%lf%d", &D, &n);
	double ans = 1e30;
	for (int i = 0; i < n; ++i) {
		double x, y;
		scanf("%lf%lf", &x, &y);
		ans = min(ans, D/((D-x)/y));
	}
	printf("%lf\n", ans);

}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int TC;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; ++tc) {
		printf("Case #%d: ", tc);
		work();
	}
	
}