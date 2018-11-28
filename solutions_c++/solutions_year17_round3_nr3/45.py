#include <bits/stdc++.h>
using namespace std;

const long double zero = 1e-9;
const int N = 60;
double A[N];

int main() {
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc) {
		int k, n;
		scanf("%d %d", &n, &k);
		double u;
		scanf("%lf", &u);
		for(int i = 1; i <= n; ++i) {
			scanf("%lf", A + i);
		}
		sort(A + 1, A + n + 1);
		A[n + 1] = 1.;

		int ls = -1;
		for(int i = 1; i <= n; ++i) {
			double diff = A[i + 1] - A[i];
			if(diff * i <= u + zero) {
				u -= diff * i;
			}
			else {
				ls = i;
				A[ls] += u / i;
				u = 0.;
				break;
			}
		}

		double ans;
		if(ls == -1) {
			ans = 1.;
		}
		else {
			ans = 1.;
			for(int i = 1; i <= ls; ++i) {
				ans *= A[ls];
			}
			for(int i = ls + 1; i <= n; ++i) {
				ans *= A[i];
			}
		}
		printf("Case #%d: %.9lf\n", tc, ans);
	}
}