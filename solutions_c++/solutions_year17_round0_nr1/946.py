#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

char s[1000005];
int k;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int test;
	scanf("%d", &test);
	int testC = 0;
	while (test --) {
		scanf("%s", s + 1);
		scanf("%d", &k);
		int n = strlen(s + 1);
		int cnt = 0;
		for (int i = 1; i <= n - k + 1; i ++) {
			if (s[i] == '+') continue;
			for (int j = i; j <= i + k - 1; j ++) {
				if (s[j] == '+') s[j] = '-';
				else s[j] = '+';
			}
			cnt ++;
		}
		bool flag = 0;
		for (int j = n - k + 2; j <= n; j ++) if (s[j] == '-') flag = 1;
		printf("Case #%d: ", ++ testC);
		if (flag) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n", cnt);
		}
	}
	return 0;
}
