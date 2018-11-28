#include <bits/stdc++.h>

#define rep(i, n) for(int i = 0; i < n; i ++)
typedef long long LL;

const int N = 1e2 + 5;
double P[N];
using namespace std;

int main() {
	int T, n, u, v, K;
	double U;
	scanf("%d", &T);
	rep(cas, T) {
		scanf("%d%d%lf", &n, &K, &U);
		rep(i, n) {
			scanf("%lf", &P[i]);
		}
		sort(P, P + n);
		double sum = 0.0;
		double answer = 0.0;
		rep(i, n) {
			sum += P[i];
			double avg = (sum + U) / (i + 1);
			double tmp = 1.0;
			rep(j, i+1) {
				tmp *= avg;
			}
			for(int j = i+1; j < n; j ++) {
				tmp *= P[j];
			}
			answer = max(answer, tmp);
		}
		printf("Case #%d: %.7f\n", cas + 1, answer);
	}
	return 0;
}
