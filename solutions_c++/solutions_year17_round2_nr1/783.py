#include <bits/stdc++.h>

using namespace std;
const int maxn = 10002;

int T, n, cas = 0;

int x[maxn], s[maxn];

int main() {
	scanf("%d", &T);
	while(T--) {
		int D;
		scanf("%d%d", &D, &n);
		double t = 0;
		for(int i = 0; i < n; ++i) {
			scanf("%d%d", &x[i], &s[i]);
			t = max(t, (D - x[i]) * 1. / s[i]);
		}
		printf("Case #%d: %lf\n", ++cas, D / t);
	}
	return 0;
}

