#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;

double p[100];

int main() {
	int t;
	scanf("%d", &t);

	for (int _ = 1; _ <= t; _++) {
		int n, k;
		double u;
		scanf("%d%d%lf", &n, &k, &u);

		for (int i = 0; i < n; i++) scanf("%lf", &p[i]);
		p[n] = 100;

		sort(p, p + n);

		for (int i = 1; i <= n; i++) {
			double need = 0;
			for (int j = 0; j < i; j++) need += p[i] - p[j];
			need = min(u, need);
			for (int j = 0; j < i; j++) p[j] += need / i;
			u -= need;
		}

		double ans = 1;
		for (int i = 0; i < n; i++) {
			ans = ans * p[i];
		}
		printf("Case #%d: %.10lf\n", _, ans);
	}
}
