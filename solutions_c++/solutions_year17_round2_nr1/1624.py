#include <cstdio>

using namespace std;

int main() {
	int t, cs;
	int d, n;
	int i;
	int k, s;
	double tt, maxT;

	scanf("%d", &t);
	for(cs = 1; cs <= t; cs++) {
		maxT = 0;
		scanf("%d%d", &d, &n);
		for(i = 0; i < n; i++) {
			scanf("%d%d", &k, &s);
			tt = (double)(d - k) / s;
			if(tt > maxT) {
				maxT = tt;
			}
		}

		printf("Case #%d: %.6f\n", cs, d/maxT);
	}
}