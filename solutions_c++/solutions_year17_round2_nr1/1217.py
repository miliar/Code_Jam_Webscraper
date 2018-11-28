#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.o", "w", stdout);
	int T;
	scanf("%d", &T);
	double D;
	int N;
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		scanf("%lf%d", &D, &N);
		double K, S;
		double time = 0;
		for (int j = 0; j < N; j++) {
			scanf("%lf%lf", &K, &S);
			double n = (D - K) / S;
			time = max(time, n);
		}
		double ans = D / time;
		printf("%lf\n", ans);
	}	
}