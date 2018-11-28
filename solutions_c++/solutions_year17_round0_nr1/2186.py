#include <stdio.h>
#include <string.h>
using namespace std;
int k, cnt;
char s[1005];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC;
	scanf("%d\n", &TC); 
	for (int tt = 1; tt <= TC; tt++) {
		scanf("%s %d\n", &s, &k); 
		cnt = 0;
		for (int i = 0; i <= strlen(s) - k; i++)
			if (s[i] == '-') {
				for (int j = i; j < i + k; j++)
					s[j] = (s[j] == '-' ? '+' : '-');
				++cnt;
			}
		bool ok = true;
		for (int i = strlen(s) - k + 1; i < strlen(s); i++)
			ok &= (s[i] == '+');

		printf("Case #%d: ", tt);
		if (ok)
			printf("%d\n", cnt);
		else
			puts("IMPOSSIBLE");
	}
}