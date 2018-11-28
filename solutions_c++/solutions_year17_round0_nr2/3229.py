#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

char N[100];

void nond(int L) {
	if (L == 1) {
		if (N[0] > '1') printf("%c", N[0] - 1);
		return;
	}

	int k = L - 1;
	for (int i = 0; i < L - 1; ++i)
		if (N[i] > N[i + 1]) {
			k = i;
			break;
		}
	if (k == L - 1) {
		if (N[L - 2] < N[L - 1]) {
			for (int i = 0; i < L - 1; ++i) printf("%c", N[i]);
			printf("%c", N[L - 1] - 1);
			return;
		} else {
			--k;
		}
	}
	nond(k + 1);
	for (int i = k + 1; i < L; ++i) printf("9");
}

void work() {
	scanf("%s", N);
	int L = strlen(N);
	bool flag = true;
	for (int i = 0; i < L - 1; ++i) 
		if (N[i] > N[i + 1]) {
			flag = false;
			break;
		}
	if (flag) printf("%s", N); else nond(L);
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
