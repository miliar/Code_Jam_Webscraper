#include <stdio.h>
#include <algorithm>
#define _USE_MATH_DEFINES
#include <math.h>

double areaH(int r, int h) {
	return M_PI * 2.0 * r * h;
}

double areaF(int r) {
	return M_PI * r * r;
}

struct pancake {
	int r, h;
	double ah;
	void calcAH() {
		ah = areaH(r, h);
	}
	bool operator<(const pancake &p) const {
		return ah > p.ah;
	}
};

void solve() {
	int used[1001] = { 0 };
	pancake pc[1001];
	int n, k;
	scanf("%d %d", &n, &k);
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &pc[i].r, &pc[i].h);
		pc[i].calcAH();
	}

	double totAH = 0;
	int bigR = 0;
	std::sort(pc, pc + n);
	int i;
	for (i = 0; i < k - 1; i++) {
		totAH += pc[i].ah;
		bigR = std::max(pc[i].r, bigR);
	}
	double bigA = 0.0;
	for (; i < n; i++) {
		double nextA = totAH +
			areaH(pc[i].r, pc[i].h) +
			areaF(std::max(bigR, pc[i].r));
		bigA = std::max(nextA, bigA);
	}

	printf("%f\n", bigA);
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
