#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <cmath>
#define Maxn 1000
using namespace std;

int t, n, k;
bool sign[Maxn + 10];

void work();
int L(int);
int R(int);

int main() {
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1;i <= t;++ i) {
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", i);
		work();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

void work() {
	memset(sign, 0, sizeof(sign));
	sign[0] = sign[n + 1] = true;
	for (int i = 1;i <= k;++ i) {
		int Min = -1, Max = -1, use;
		//printf("set %d:\n", i);
		for (int j = 1;j <= n;++ j)
			if (!sign[j]) {
				int l = L(j), r = R(j);
				//printf("L: %d	R: %d\n", l, r);
				if (Min < min(l, r) || Min == -1 ) {
					use = j;
					Min = min(l, r);
					Max = max(l, r);
				}
				else if(Min == min(l, r) && Max < max(l, r)) {
					use = j;
					Min = min(l, r);
					Max = max(l, r);
				}
			}
		sign[use] = true;
		//printf("%d set at %d\n", i, use);
		if (i == k)
			printf("%d %d\n", Max, Min);
	}
}

int L(int x) {
	int temp = x;
	do {
		-- temp;
	} while(!sign[temp]);
	return x - temp - 1;
}

int R(int x) {
	int temp = x;
	do {
		++ temp;
	} while(!sign[temp]);
	return temp - x - 1;
}
