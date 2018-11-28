#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <omp.h>
using namespace std;

const int mn = 1010;
int k[mn], s[mn];

bool check(double speed, int *k, int *s, int n, double D) {
	for (int i = 0; i < n; ++i) {
		if (s[i] >= speed) continue;
		double time = k[i] / (speed - s[i]);
		if (speed * time < D) return 0;
	}
	return 1;
}

int main() {
	int Tn;
	scanf("%d", &Tn);

	for (int Tc = 1; Tc <= Tn; ++Tc) {
		double ans = 0;
		int D, n;
		scanf("%d%d",&D, &n);
		for (int i = 0; i < n; ++i)
			scanf("%d%d", &k[i], &s[i]);
		double l = 0, r = D * 1e6, m;
		int times = 0;
		while (l < r && ++times < 200) {
			m = (l + r) / 2.0;
			if (check(m, k, s, n, D)) {
				ans = m;
				l = m;
			} else {
				r = m;
			}
		}


		printf("Case #%d: ", Tc);
		printf("%.10f\n", ans);
	}
	return 0;
}
