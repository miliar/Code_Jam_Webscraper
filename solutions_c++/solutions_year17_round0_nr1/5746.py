#include <cstdio>
#include <cstring>
#define N 10001
int tc, tcn, n, k, len, pos, num;
char s[N];



void solve() {
	scanf("%d", &tc);
	while (tc--) {
		scanf("%s %d", s, &k);
		len = strlen(s);
		pos = 1;
		num = 0;
		for (int j = 0; j < len; j++) {
			if (s[j] == '+')
				continue;
			if (j + k - 1 >= len) {
				pos = 0;
			}
			for (int t = 1; t < k; t++) {
				if (s[j + t] == '+')
					s[j + t] = '-';
				else
					s[j + t] = '+';
			}

			num++;
		}

		printf("Case #%d: ", ++tcn);
		if (!pos)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", num);
	}


}

int main(void) {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	solve();
	return 0;
}