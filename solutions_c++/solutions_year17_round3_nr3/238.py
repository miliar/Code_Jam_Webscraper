#include <stdio.h>
#include <algorithm>

void solve() {
	double tot[51];
	int n, k;
	scanf("%d %d", &n, &k);
	double u;
	scanf("%lf", &u);
	for (int i = 0; i < n; i++) {
		scanf("%lf", &tot[i]);
	}
	std::sort(tot, tot + n);
	tot[n] = 1e100;
	double used = 0.0;
	int amt = 0;
	double curr = tot[0];
	for (int i = 0; i < n; i++) {
		amt++;
		double take1 = tot[i + 1] - tot[i];
		double take2 = (u - used) / amt;
		if (take1 < take2) {
			used += take1 * amt;
			curr += take1;
		}
		else {
			used += take2 * amt;
			curr += take2;
			break;
		}
	}
	for (int i = 0; i < amt; i++) {
		tot[i] = curr;
	}

	double chance = 1.0;
	for (int i = 0; i < n; i++) {
		chance *= tot[i];
	}
	printf("%lf\n", chance);
}

int main() {
	int T;
	scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);
		solve();
	}

	return 0;
}
