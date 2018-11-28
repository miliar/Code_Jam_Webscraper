#include <cstdio>
#include <algorithm>
using namespace std;

int k[1000], s[1000];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int TN=1; TN<=T; ++TN) {
		int d, n;
		scanf("%d%d", &d, &n);
		for (int i=0; i<n; ++i)
			scanf("%d%d", k+i, s+i);
		double ans = 0;
		for (int i=0; i<n; ++i)
			ans = max(ans, (double)(d-k[i])/s[i]);
		printf("Case #%d: ", TN);
		printf("%.10f\n", d/ans);
	}
	return 0;
}