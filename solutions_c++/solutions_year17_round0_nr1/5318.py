#include <cstdio>
#include <cstring>
using namespace std;

int main() {
	int t, k;
	char s[1001];
	//freopen("A-large.in", "r", stdin);
	//freopen("output.txt", "w", stdout);

	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		int ans = 0;
		scanf("%s %d", s, &k);
		int len = strlen(s);
		for (int i = 0; i < len; i++) {
			if (s[i] == '-') {
				if (i > len - k) {
					ans = -1;
					break;
				}
				ans++;
				for (int j = i; j < i + k; j++) {
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}	
			}
		}
		if (ans == -1)
			printf("Case #%d: IMPOSSIBLE\n", tc);
		else
			printf("Case #%d: %d\n", tc, ans);
	}
}