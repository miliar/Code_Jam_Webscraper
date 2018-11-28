#include <cstdio>
#include <cstring>
using namespace std;

void flip(char *s, int j, int k)
{
	for (int a = j; a < j + k; a++) {
		s[a] = (s[a] == '-') ? '+' : '-';
	}
}

int main() {
	int t, k;
	char s[1002];
	scanf("%d\n", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%s %d", s, &k);
		int d = strlen(s);
		int ans = 0;
		for (int j = 0; j <= d - k; j++) {
			if (s[j] == '-') {
				flip(s, j, k);
				ans++;
			}
		}
		for (int j = d - k + 1; j < d; j++) {
			if (s[j] == '-') {
				ans = -1;
				break;
			}
		}
		if (ans >= 0) {
			printf("Case #%d: %d\n", i, ans);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", i);
		}
	}
	return 0;
}
