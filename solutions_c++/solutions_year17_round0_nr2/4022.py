#include <cstdio>
#include <cstring>

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d\n", &T);
	for (int kase = 1; kase <= T; ++kase) {
		char s[20], t[20];
		scanf("%s\n", s);
		int l = strlen(s), i;
		bool ok = true;
		for (i = 0; i < l; ++i) {
			if (!ok) break;
			if (i < l - 1 && s[i + 1] <= s[i])
				for (int j = i; j < l; ++j) {
					if (s[j] < s[i]) {
						ok = false;
						break;
					}
				}
			t[i] = s[i] - !ok;
		}
		for (; i < l; ++i)
			t[i] = '9';
		t[l] = 0;
		for (i = 0; i < l && t[i] == '0'; ++i);
		printf("Case #%d: %s\n", kase, t + i);
	}
	return 0;
}

