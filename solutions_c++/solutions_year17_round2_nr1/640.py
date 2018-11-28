#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		int L, n;
		scanf("%d%d", &L, &n);
		double mm = 0;
		for (int i = 1; i <= n; ++i) {
			int x, y;
			scanf("%d%d", &x, &y);
			mm = max(1.0 * (L - x) / y, mm);
		}
		printf("Case #%d: %.10lf\n", cas, L / mm);
	}
	return 0;
}
