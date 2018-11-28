#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int D, n, k, s;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		double mt = 0;
		scanf("%d%d", &D, &n);
		for (int i = 0; i < n; i++) {
			scanf("%d%d", &k, &s);
			mt = max(mt, (D-k)*1.0/s);
		}
		printf("Case #%d: %.7lf\n", cas, D/mt);
	}
	return 0;
}