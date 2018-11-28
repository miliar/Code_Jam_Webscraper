#include <cstdio>
#include <math.h>
#include <algorithm>

using namespace std;

int t, T;
int N, P;
int r[100];
int q[100][100];
int iter[100];

int main() {
	int i, j;
	scanf("%d", &T);
	for(t = 1; t <= T; t++) {
		scanf("%d %d", &N, &P);
		for(i = 0; i < N; i++) {
			scanf("%d", &r[i]);
			iter[i] = 0;
		}
		for(i = 0; i < N; i++) {
			for(j = 0; j < P; j++) {
				scanf("%d", &q[i][j]);
			}
			std:sort(q[i], q[i]+P);
		}
		bool flag = false;
		int count = 0;
		while(!flag) {
			int mini = 0;
			i = 0;
			double min = 1.0 * q[i][iter[0]] / r[i];
			int left = ceil(q[i][iter[0]] / (1.1 * r[i]));
			int right = floor(q[i][iter[0]] / (0.9 * r[i]));
			for(i = 1; i < N; i++) {
				int x = ceil(q[i][iter[i]] / (1.1 * r[i]));
				int y = floor(q[i][iter[i]] / (0.9 * r[i]));
				if(x > left) left = x;
				if(y < right) right = y;
				if(min > 1.0 * q[i][iter[i]] / r[i]) {
					min = 1.0 * q[i][iter[i]] / r[i];
					mini = i;
				}
			}
			if(left <= right) {
				count++;
				for(i = 0; i < N; i++) {
					if(++iter[i] >= P) flag = true;
				}
			} else {
				if(++iter[mini] >= P) flag = true;
			}
		}
		printf("Case #%d: %d\n", t, count);
	}
	return 0;
}
