#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int N = 1000;
const double PI = 3.1415926535897932;

struct Pancake {
	int r, h;
} a[N];
int n, m;

bool cmpR(const Pancake &a, const Pancake &b) {
	return a.r > b.r;
}

bool cmpA(const Pancake &a, const Pancake &b) {
	return 1LL * a.r * a.h > 1LL * b.r * b.h;
}

int main() {
	int testCases;
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			scanf("%d%d", &a[i].r, &a[i].h);
		}

		double ret = 0.0;
		for (int i = 0; i + m <= n; ++i) {
			double area = 0.0;
			sort(a + i, a + n, cmpR);
			area += PI * a[i].r * a[i].r;
			sort(a + i + 1, a + n, cmpA);
			for (int j = 0; j < m; ++j) {
				area += 2 * PI * a[i + j].r * a[i + j].h;
			}
			ret = max(ret, area);
		}

		printf("Case #%d: %.10f\n", _, ret);
	}
	return 0;
}
