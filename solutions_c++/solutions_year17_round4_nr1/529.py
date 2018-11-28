#include <cstdio>
#include <math.h>
#include <algorithm>

using namespace std;

int t, T;
int N, P;
int c[4];


int main() {
	int i, j, tmp, a;
	scanf("%d", &T);
	for(t = 1; t <= T; t++) {
		scanf("%d %d", &N, &P);
		for(i = 0; i < P; i++) {
			c[i] = 0;
		}
		for(i = 0; i < N; i++) {
			scanf("%d", &tmp);
			c[tmp%P]++;
		}
		printf("Case #%d: ", t);
		if(P == 2) {
			printf("%d", c[0] + (c[1]+1) / 2);
		} else if(P == 3) {
			if(c[1] > c[2]) {
				printf("%d", c[0] + c[2] + (c[1] - c[2] + 2) / 3);
			} else {
				printf("%d", c[0] + c[1] + (c[2] - c[1] + 2) / 3);
			}
		} else if(P == 4) {
			a = c[0];
			if(c[1] < c[3]) {
				tmp = c[3];
				c[3] = c[1];
				c[1] = tmp;
			}
			a += c[3];
			a += c[2] / 2;
			a += (c[1] - c[3]) / 4;
			if(c[2] % 2 > 0 && (c[1] - c[3]) % 4 >= 2) {
				a++;
				c[2] -= 1;
				c[1] -= 2;
			}
			if(c[2] % 2 > 0 || (c[1] - c[3]) % 4 > 0) a++;
			printf("%d", a);
		}
		printf("\n");
	}
	return 0;
}
