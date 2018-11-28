#include <cstdio>
#include <iostream>
#include <memory.h>
#include <queue>
#include <stack>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T;
	scanf("%d",&T);
	for (int tc = 1; tc <= T; tc++) {
		int N,K;
		scanf("%d %d",&N,&K);
		double U;
		scanf("%lf",&U);
		double P[55];
		for (int i = 0; i < N; i++) {
			scanf("%lf",&P[i]);
		}
		sort(P, P + N);
		for (int i = 1; i < N; i++) {
			double diff = P[i] - P[i-1];
			if (diff * (double)i <= U) {
				for (int j = 0; j < i; j++) {
					P[j] = P[i];
				}
				U -= diff*(double)i;
			}
			else {
				for (int j = 0; j < i; j++) {
					P[j] += (U / (double)i);
				}
				U = 0.0;
				break;
			}
		}
		U /= (double) N;
		double res = 1;
		for (int i = 0; i < K; i++) {
			res *= (P[i] + U);
		}
		printf("Case #%d: %.6lf\n", tc, res);
	}
	return 0;
}