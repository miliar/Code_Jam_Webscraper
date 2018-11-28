#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define PI 3.141592653589793

struct Pancake {
	double radius, height;
};
int T;
int N, K;
Pancake P[1001];
double d[1001][1001];

bool order(const Pancake &x, const Pancake &y) {
	if (x.radius > y.radius) return true;
	else return false;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	int i, j, k;

	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d %d", &N, &K);
		for (i = 1; i <= N; i++)
			scanf("%lf %lf", &P[i].radius, &P[i].height);

		sort(P + 1, P + N + 1, order);

		for (i = 1; i <= K; i++) {
			for (j = 1; j <= N; j++)
				d[i][j] = 0;
		}

		for (i = 1; i <= N; i++)
			d[1][i] = PI*P[i].radius*P[i].radius + 2 * PI*P[i].radius*P[i].height;
		for (i = 2; i <= K; i++) {
			for (j = 1; j <= N; j++) {
				for (k = 1; k < j; k++) {
					if (d[i][j] < d[i - 1][k] + 2 * PI*P[j].radius*P[j].height)
						d[i][j] = d[i - 1][k] + 2 * PI*P[j].radius*P[j].height;
				}
			}
		}

		double res = 0;
		for (i = 1; i <= N; i++) {
			if (res < d[K][i]) res = d[K][i];
		}

		printf("Case #%d: ", t);
		printf("%lf", res);
		printf("\n");
	}
	return 0;
}