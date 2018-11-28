#include <cstdio>
#include <cstring>

int T;
char N[50], Ans[50];
int ss;

bool bt(int p) {
	if (p == ss - 1) {
		for (int i = 0; i < ss; i++) {
			if (N[i] != '0') {
				strcpy(Ans, N + i);
				return true;
			}
		}
	}
	else {
		while (N[p] <= N[p + 1]) {
			if (bt(p + 1)) return true;
			N[p + 1]--;
		}
		for (int i = p + 1; i < ss; i++) N[i] = '9';
		return false;
	}
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%s", N);
		ss = strlen(N);
		// is it tidy?
		while (!bt(0)) {
			N[0]--;
			for (int i = 1; i < ss; i++) N[i] = '9';
		}
		printf("Case #%d: %s\n", tc, Ans);
	}
	return 0;
}