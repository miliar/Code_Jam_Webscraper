#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

char st[2000];
int K;

void work() {
	scanf("%s%d", st, &K);
	int L = strlen(st);
	int ans = 0, l = 0, r = 0;
	for (int i = 0; i <= L - K; ++i) {
		if (l <= i && i < r) {
			if (st[i] == '-') st[i] = '+'; else st[i] = '-';
			l = i + 1;
		}
		if (st[i] == '-') {
			++ans;
			l = max(r, i + 1); r = i + K;
		}
	}
	for (int i = L - K + 1; i < L; ++i) {
		if (l <= i && i < r) {
			if (st[i] == '+') {
				printf("IMPOSSIBLE\n");
				return;
			}
		} else {
			if (st[i] == '-') {
				printf("IMPOSSIBLE\n");
				return;
			}
		}
	}
	printf("%d\n", ans);
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
