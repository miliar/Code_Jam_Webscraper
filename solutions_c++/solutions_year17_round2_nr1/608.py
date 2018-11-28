#include <cstdio>
#include <math.h>
#include <algorithm>

using namespace std;

int t, T;
int N, D;
int k;
int s;

int main() {
	int i, j;
	scanf("%d", &T);
	for(t = 1; t <= T; t++) {
		scanf("%d %d", &D, &N);
		double time = 0;
		for(i = 0; i < N; i++) {
			scanf("%d %d", &k, &s);
			if((D - k) * 1.0 / s > time) time = (D - k) * 1.0 / s;
		}
		printf("Case #%d: %lf\n", t, D / time);
	}
	return 0;
}
