#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	int N, K;
	int count = 1;
	while(scanf("%d%d", &N, &K) != EOF) {
		vector<double> v(N);
		double U;
		scanf("%lf", &U);
		for (int i = 0; i < N; i++) {
			scanf("%lf", &v[i]);
		}
		sort(v.begin(), v.end());
		vector<double> sum(N);
		sum[0] = v[0];
		for (int i = 1; i < N; i++) {
			sum[i] = v[i] + sum[i - 1];
		}
		int d = -1;
		for (int i = 0; i < N; i++) {
			if (v[i] * (i + 1) - sum[i] > U) {
				d = i - 1;
				
				break;
			}
		}
		if (d == -1) {
			d = N - 1;
		}
		double p = 1;
		double pi = min(1.0, (U + sum[d]) / (d + 1));
		for (int i = 0; i <= d; i++) {
			p *= pi;
		}
		for (int i = d + 1; i < N; i++) {
			p *= v[i];
		}
		printf("Case #%d: %.8lf\n", count++, p);
	}
}