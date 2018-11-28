#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const int MAXN = 1101;
char str[MAXN];

int main() {
	int t, ca = 1, k;
	scanf("%d", &t);
	while (t--) {
		scanf("%s%d", str, &k);
		int len = strlen(str), ans = 0, flag = 1;
		for (int i = 0; i < len; i++) {
			if (str[i] == '-' && i + k <= len) {
				for (int j = i; j < i + k; j++) {
					if (str[j] == '-') str[j] = '+';
					else str[j] = '-';
				}
				ans++;
			} else if (str[i] == '-') {
				printf("Case #%d: IMPOSSIBLE\n", ca);
				flag = 0;
				break;
			}
		}
		if (flag) printf("Case #%d: %d\n", ca, ans);
		ca++;
	}
}
