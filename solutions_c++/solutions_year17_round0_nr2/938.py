#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

char s[1000005];
int ans[1000005];
int n;

void solve() {
	bool isOK = 0;
	for (int i = 1; i <= n; i ++) {
		for (int k = 9; k >= 0; k --) {
			for (int j = i; j <= n; j ++) {
				ans[j] = k;
			}
			bool isOK = 1;
			for (int j = 1; j <= n; j ++) {
				if (ans[j] < s[j] - '0') {
					isOK = 1;
					break;
				}
				if (ans[j] > s[j] - '0') {
					isOK = 0;
					break;
				}
			}
			if (isOK) {
				break;
			}
		}
	}
}

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int test;
	scanf("%d", &test);
	int testC = 0;
	while (test --) {
		scanf("%s", s + 1);
		n = strlen(s + 1);
		solve();
		int pos = n;
		for (int i = 1; i <= n; i ++) {
			if (ans[i] != 0) {
				pos = i;
				break;
			}
		}
		printf("Case #%d: ", ++ testC);
		for (int i = pos; i <= n; i ++) printf("%d", ans[i]);
		puts("");
	}
	return 0;
}
