#include <bits/stdc++.h>

using namespace std;

int k;
char str[100001];

int main( ) {
	int T, tp = 0;
	scanf("%d", &T);
	for (int i = 1; i <= T; i ++) {
		scanf("%s", str + 1);
		scanf("%d", &k);
		int cnt = 0;
		bool ok = false;
		int n = (int )strlen(str + 1);
		for (int j = 1; j <= n; j ++) {
			if (str[j] == '+') continue;
			if (j + k - 1 > n) {
				ok = true;
				break;
			}
			for (int r = j; r <= j + k - 1; ++ r)
				if (str[r] == '+') str[r] = '-';
				else str[r] = '+';
			++ cnt;
		}
		printf("Case #%d: ", ++ tp);
		if (ok) printf("IMPOSSIBLE\n");
		else printf("%d\n", cnt);
	}
	return 0;
}
