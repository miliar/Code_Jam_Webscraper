#include <cstdio>
#include <cstring>

bool f(int idx, int num[], int prev, int len) {

	while (num[idx] >= prev) {
		if (idx == len - 1) return true;
		if (f(idx + 1, num, num[idx], len)) return true;
		num[idx]--;
		for (int i = idx+1; i < len; i++) num[i] = 9;
	}

	return false;
}

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		int res[30];
		char num[30];
		scanf("%s", num);
		int len = strlen(num);

		for (int i = 0; i < len; i++) {
			res[i] = num[i] - '0';
		}

		f(0, res, 0, len);

		printf("Case #%d: ", t);
		for (int i = 0; i < len; i++) {
			if (i == 0 && res[i] == 0) continue;
			printf("%d", res[i]);
		}
		printf("\n");
	}

	return 0;
}