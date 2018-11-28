#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <queue>

using namespace std;

int n, p, res, f[5];

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("choco.out", "w", stdout);
	int test; scanf("%d", &test);
	for(int t = 1; t <= test; t++) {
		printf("Case #%d: ", t);
		res = 0;
		scanf("%d%d", &n, &p);
		for(int i = 0; i <= 3; i++) f[i] = 0;
		for(int i = 0; i < n; i++) {
			int x; scanf("%d", &x);
			++f[(x % p)];
		}
		if (p == 2) {
			res = n - (f[1] / 2);
		}
		else if (p == 3) {
			int rem = min(f[1], f[2]);
			f[1] -= rem;
			f[2] -= rem;
			if (f[1] > 0) rem += f[1] - ((f[1] / 3) + (f[1] % 3 != 0));
			if (f[2] > 0) rem += f[2] - ((f[2] / 3) + (f[2] % 3 != 0));
			res = n - rem;
		}
		else {
			int rem = min(f[1], f[3]);
			f[1] -= rem;
			f[3] -= rem;
			if (f[1] > 0) rem += f[1] - ((f[1] / 4) + (f[1] % 4 != 0));
			if (f[3] > 0) rem += f[3] - ((f[3] / 4) + (f[3] % 4 != 0));
			rem += f[2] / 2;
			res = n - rem;
		}
		printf("%d\n", res);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}