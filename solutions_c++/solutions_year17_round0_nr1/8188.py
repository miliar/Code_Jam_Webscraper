#include <cstdio>
#include <cstring>

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	

	for (int t = 1; t <= T; t++) {
		int num[1001];
		char s[1001];
		scanf("%s", s);
		int k;
		scanf("%d", &k);

		int len = strlen(s);
		for (int i = 0; i < len; i++) {
			if (s[i] == '+') num[i] = 1;
			else num[i] = 0;
		}

		int cnt = 0;
		for (int i = 0; i < len; i++) {
			if (num[i] % 2 == 1) continue;
			cnt++;
			for (int j = i; j < i + k && i + k <= len; j++) {
				num[j]++;
			}
		}

		bool success = true;
		for (int i = len - 1; i >= len - k; i--) {
			if (num[i] % 2 != 1) {
				success = false;
				break;
			}
		}

		if (success) printf("Case #%d: %d\n", t, cnt);
		else printf("Case #%d: IMPOSSIBLE\n", t);
	}

	return 0;
}