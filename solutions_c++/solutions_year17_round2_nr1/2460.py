// Problem A. Steed 2: Cruise Control
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		int d, n, k, s;
		scanf("%d %d", &d, &n);
		double ans = -1;
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &k, &s);
			double t = (double) (d - k) / s;
			if (ans < 0 || t > ans) ans = t;
		}

		printf("Case #%d: %0.6f\n", ti, (double) d / ans);
	}

	return 0;
}
