#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

#define MAXX(x, y) ((x)=max((x),(y)))

int c[5], f[105][105][105];

int main() {
	int Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; test++) {
		int N, P;
		scanf("%d%d", &N, &P);
		memset(c, 0, sizeof(c));
		for (int i = 0, x; i < N; i++) {
			scanf("%d", &x);
			c[x % P]++;
		}
		printf("Case #%d: ", test);
		if (P == 2) {
			printf("%d\n", c[0] + (c[1] + 1) / 2);
			continue;
		}
		int c0 = c[0];
		N -= c[0];
		memset(f, -60, sizeof(f));
		f[N][c[1]][c[2]] = 0;
		for (int i = N; i >= 1; i--)
			for (int c1 = 0; c1 <= c[1]; c1++)
				for (int c2 = 0; c2 <= c[2]; c2++) {
					if (i == 2 && c1 == 1 && c2 == 1)
						int asd=1;
					int d = f[i][c1][c2];
					if (d < 0) continue;
					int c3 = i - c1 - c2;
					int r = ((c[1] - c1) * 1 + (c[2] - c2) * 2 + (c[3] - c3) * 3) % P;
					d += (r == 0);
					if (c1 > 0) MAXX(f[i - 1][c1 - 1][c2], d);
					if (c2 > 0) MAXX(f[i - 1][c1][c2 - 1], d);
					if (c3 > 0) MAXX(f[i - 1][c1][c2], d);
				}
		printf("%d\n", c0 + f[0][0][0]);
	}
	return 0;
}