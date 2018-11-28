#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;

const int N = 50 + 1;

double a[N];
int n, m;
double u;

int main() {
	int testCases;
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		scanf("%d%d", &n, &m);
		scanf("%lf", &u);
		for (int i = 0; i < n; ++i) {
			scanf("%lf", &a[i]);
		}
		sort(a, a + n);
		a[n] = 1.0;
		while (u > 0 && a[0] < 1.0) {
			for (int i = 0; i < n; ++i) {
				if (a[i] < a[i + 1]) {
					double delta = min((a[i + 1] - a[i]) * (i + 1), u);
					u -= delta;
					delta /= i + 1;
					for (int j = 0; j <= i; ++j) {
						a[j] += delta;
					}
					break;
				}
			}
		}

		double ret = 1.0;
		for (int i = 0; i < n; ++i) {
			ret *= a[i];
		}
		printf("Case #%d: %.20f\n", _, ret);
	}
	return 0;
}
