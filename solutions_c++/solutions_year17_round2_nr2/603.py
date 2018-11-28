#include <cstdio>
#include <math.h>
#include <algorithm>

using namespace std;

int t, T;
int N;
int c[6];
int s;
int y;
bool imp;
char ch[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};

int tr(int x) {
	return (x + y) % 6;
}

int sh(int x, int y) {
	if(x + y == 2) return 1;
	else if(x + y == 4) return 5;
	else if(x + y == 6) return 3;
}

int main() {
	int i, j;
	scanf("%d", &T);
	for(t = 1; t <= T; t++) {
		scanf("%d", &N);
		for(i = 0; i < 6; i++) {
			scanf("%d", &c[i]);
		}
		printf("Case #%d: ", t);
		if(c[0] >= c[2] && c[0] >= c[4]) {
			y = 0;
		} else if(c[2] >= c[4] && c[2] >= c[0]) {
			y = 2;
		} else {
			y = 4;
		}
		if(c[tr(0)] <= c[tr(2)] + c[tr(4)]) {
			for(i = 0; i < c[tr(0)]; i++) {
				printf("%c", ch[tr(0)]);
				if(i < c[tr(2)]) {
					printf("%c", ch[tr(2)]);
				}
				if(c[tr(0)] - i - 1 < c[tr(4)]) {
					printf("%c", ch[tr(4)]);
				}
			}
		} else {
			printf("IMPOSSIBLE");
		}
		printf("\n");
	}
	return 0;
}
