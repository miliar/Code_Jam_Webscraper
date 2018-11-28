#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int cmp(const void *a, const void *b) {
	return (*(int *)a - *(int *)b);
}

int main() {
	int T, N, P;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		scanf("%d %d", &N, &P);
		int R[50] = {};
		int Q[50][50] = {};
		int Qmin[50][50] = {};
		int Qmax[50][50] = {};
		for (int j = 0; j < N; j++) {
			scanf("%d", &R[j]);
		}
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < P; k++) {
				scanf("%d", &Q[j][k]);
			}
			qsort(Q[j], P, sizeof(int), cmp);
			for (int k = 0; k < P; k++) {
				Qmin[j][k] = (int)ceil((double)Q[j][k] / ((double)R[j] * 1.1));
				Qmax[j][k] = (int)floor((double)Q[j][k] / ((double)R[j] * 0.9));
			}
		}
		int count = 0;
		bool stop = false;
		int index[50] = {};
		while(!stop) {
			int min = 0, max = 1000000;
			int k = Qmin[0][index[0]], kIndex = 0;
			for (int j = 0; j < N; j++) {
				if (Qmin[j][index[j]] > min) min = Qmin[j][index[j]];
				if (Qmax[j][index[j]] < max) max = Qmax[j][index[j]];
				if (Qmin[j][index[j]] < k) {
					k = Qmin[j][index[j]];
					kIndex = j;
				}
			}
			if (min <= max) {
				count++;
				for (int j = 0; j < N; j++) {
					index[j]++;
					stop = stop || (index[j] == P);
				}
			} else {
				index[kIndex]++;
				stop = (index[kIndex] == P);
			}
		}
		printf("Case #%d: %d\n", i + 1, count);
	}
	return 0;
}

