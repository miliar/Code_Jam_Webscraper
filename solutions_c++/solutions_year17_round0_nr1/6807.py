#include <cstdio>
#include <iostream>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	int cnt = 0;
	while (t--) {
		cnt++;
		int k;
		char st[1024] = { 0 };
		scanf("%s %d", st, &k);

		int res = 0;
		for (int i = 0; st[i]; i++) {
			if (st[i] == '-') {
				int l = k;
				int j = i;
				while (st[j] && l) {
					st[j] = st[j] == '+' ? '-' : '+';
					j++;
					l--;
				}
				if (l) {
					res = -1;
					break;
				}
				res++;
			}
		}

		for (int i = 0; st[i]; i++)
			if (st[i] == '-') {
				res = -1;
				break;
			}

		printf("Case #%d: ", cnt);
		if (res == -1) {
			puts("IMPOSSIBLE");
		}
		else {
			printf("%d\n", res);
		}
	}

	return 0;
}