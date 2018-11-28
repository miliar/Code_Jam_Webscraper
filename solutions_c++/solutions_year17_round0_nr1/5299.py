#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
char s[1005];
int K, ok;
int main() {
	int T; for (scanf("%d", &T); T--; ) {
		scanf("%s%d", s + 1, &K);
		int n = strlen(s + 1);
		int res = 0;
		for (int i = 1; i <= n - K + 1; i++) {
			if (s[i] == '-') {
				for (int j = i; j <= i + K - 1; j++) s[j] = (s[j] == '+' ? '-' : '+');
				res++;
			}
		}
		ok = 1;
		for (int i = n - K + 1; i <= n; i++) if (s[i] == '-') ok = 0;
		static int tc = 0;
		printf("Case #%d: ", ++tc);
		if (ok) printf("%d\n", res);
		else puts("IMPOSSIBLE");
	}
}