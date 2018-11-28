#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

#define eps 1e-12

bool equal(const double a, const double b) {
	return abs(a - b) < eps;
}

double Redistribute(vector<double> p, const int N, const int K, double U) {
	sort(p.begin(), p.end());
	while (U > eps) {
		int lastPoz = 0;
		while (lastPoz < N && p[lastPoz] == p[0]) {
			lastPoz++;
		}
		const double nextThreashold = lastPoz < N ? p[lastPoz] : 1.0;
		const double needAll = (nextThreashold - p[0]) * lastPoz;
		const double nextVal = (U + eps >= needAll) ? nextThreashold : (p[0] + U / lastPoz);
		U -= (nextVal - p[0]) * lastPoz;
		for (int i = 0; i < lastPoz; i++) {
			p[i] = nextVal;
		}
	}
	double prod = 1.0;
	for (int i = 0; i < N; i++) {
		prod *= p[i];
	}
	return prod;
}

void Solve() {
	int N, K;
	double U;
	scanf("%d %d %lf", &N, &K, &U);
	vector<double> probCrash(N);
	for (int i = 0; i < N; i++) {
		scanf("%lf", &probCrash[i]);
	}
	printf("%.8lf\n", Redistribute(probCrash, N, K, U));
}

int main() {
	freopen("data.in", "rb", stdin);
	freopen("data.out", "wb", stdout);
	int tst;
	scanf("%d", &tst);
	for (int index = 1; index <= tst; index++) {
		printf("Case #%d: ", index);
		Solve();
	}
	return 0;
}