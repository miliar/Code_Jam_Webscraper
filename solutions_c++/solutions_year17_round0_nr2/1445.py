#include <bits/stdc++.h>
using namespace std;

int T, n;
char s[100001];

int main()
{
	
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	
	scanf("%d", &T);
	for (int Case = 1; Case <= T; ++ Case)
	{
		printf("Case #%d: ", Case);
		scanf("%s", s + 1);
		n = strlen(s + 1);
		if (n == 1) printf("%c\n", s[1]);
		else {
			int j;
			for (j = 1; j <= n && s[j] >= s[j - 1]; ++ j);
			if (j > n)
			{
				printf("%s\n", s + 1);
			} else {
				int k;
				for (k = j - 1; k >= 1; -- k)
					if (s[k] - 1 >= s[k - 1]) break;
				for (int i = 1; i < k; ++ i) printf("%c", s[i]);
				if (s[k] != '1') printf("%c", s[k] - 1);
				for (int i = k + 1; i <= n; ++ i) printf("9");
				printf("\n");
			}
		}
	}
	return 0;
}

