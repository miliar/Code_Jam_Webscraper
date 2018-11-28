#include <bits/stdc++.h>

using namespace std;

int t, d, n, td, ts;
pair<int, char> c[3];
char ans[1005];

int main() {
	freopen ("inn","r",stdin);
	freopen ("myfile.txt","w",stdout);
	scanf("%d", &t);
	for (int kk = 1; kk <= t; kk++) {
		scanf("%d", &n);
		memset(ans, '@', sizeof(ans));
		for (int j = 0; j < 6; j++) {
			scanf("%d", &d);
			if (j % 2 == 0) {
				if (j / 2 == 0)
					c[j / 2] = make_pair(d, 'R');
				if (j / 2 == 1) {
					c[j / 2] = make_pair(d, 'Y');
				}
				if (j / 2 == 2) {
					c[j / 2] = make_pair(d, 'B');
				}
			}
		}
		sort(c, c + 3);
		if (c[2].first > n / 2) {
			printf("Case #%d: IMPOSSIBLE\n", kk);
		} else {
			int st = 0;
			while (c[2].first--) {
				ans[st] = c[2].second;
				st += 2;
			}
			if (n % 2 == 0) {
				st = n - 1;
			} else {
				st = n - 2;
			}
			while (c[1].first--) {
				while (ans[st] != '@') {
					st--;
					st %= n;
				}
				ans[st] = c[1].second;
				st -= 2;
				st %= n;
			}
			st = 0;
			while (c[0].first--) {
				while (ans[st] != '@') {
					st++;
					st %= n;
				}
				ans[st] = c[0].second;
			}
			printf("Case #%d: ", kk);
			for (int j = 0; j < n; j++) {
				printf("%c", ans[j]);
			}
			printf("\n");
		}
	}
	return 0;
}
