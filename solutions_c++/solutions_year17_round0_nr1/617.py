#include <bits/stdc++.h>

using namespace std;

int t,n,k;
char s[1001];

int main() {
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%s%d", s, &k);
		n = strlen(s);
		int h = 0;
		for (int i = 0; i < n - k + 1; i++)
			if (s[i] == '-') {
				h++;
				for (int j = i; j < i + k; j++)
					s[j] = s[j] == '+' ? '-' : '+';
			}
		for (int i = n - k; h >= 0 && i < n; i++)
			if (s[i] != '+')
				h = -1;
		if (h > -1)
			printf("Case #%d: %d\n", tc, h);
		else
			printf("Case #%d: IMPOSSIBLE\n", tc);
	}
	return 0;
}