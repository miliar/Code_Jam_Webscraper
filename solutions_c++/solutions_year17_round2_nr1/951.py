#include <cstdio>                        
#include <cassert>
#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;

#define eps 1e-8

int test, pos[2000], speed[2000], t, d, n;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	scanf("%d", &t);

	for (int test = 1; test <= t; ++test) {
		scanf("%d%d", &d, &n);
		double ans = 0.0;
		for (int i = 1; i <= n; ++i) {
			scanf("%d%d", &pos[i], &speed[i]);
			ans = max(ans, (d - pos[i] + 0.0) / speed[i]);
		}

		printf("Case #%d: %.10lf\n", test, d / ans);
	}
}