#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

int N, R, O, Y, G, B, V;

char ans[2000];

void run(int a, int b, int c, char x, char y, char z) {
	for (int i = 0; i < N; i += 2) {
		if (a > 0) {
			ans[i] = x;
			--a;
		} else if (b > 0) {
			ans[i] = y;
			--b;
		}
	}
	for (int i = 1; i < N; i += 2) {
		if (b > 0) {
			ans[i] = y;
			--b;
		} else {
			ans[i] = z;
			--c;
		}
	}
}

void work() {
	scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
	if (R > N / 2 || Y > N / 2 || B > N / 2) {
		printf("IMPOSSIBLE\n");
		return;
	}

	if (R >= Y && R >= B) {
		run(R, Y, B, 'R', 'Y', 'B');
	} else
	if (Y >= R && Y >= B) {
		run(Y, R, B, 'Y', 'R', 'B');
	} else {
		run(B, R, Y, 'B', 'R', 'Y');
	}
	
	for (int i = 0; i < N; ++i) printf("%c", ans[i]);
	printf("\n");
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: ", i + 1);
		work();
	}
	return 0;
}
