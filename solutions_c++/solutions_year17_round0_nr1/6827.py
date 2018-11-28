#include <stdio.h>
#define INF 987654321

char s[1005];
int L, k;

int solve()
{
	int res = 0;
	for (int i = 0; i <= L-k; i++)
	{
 		if (s[i] == '-')
		{
			for (int j = i; j < i+k; j++)
				s[j] = s[j] == '-' ? '+' : '-';
			res++;
		}
	}
	for (int i = 0; i < L; i++)
		if (s[i] == '-') return INF;
	return res;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%s %d", &s, &k);
		L = 0;
		for (int i = 0; s[i]; i++) L++;
		int res = solve();
		printf("Case #%d: ", t);
		if (res == INF)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", res);
	}
	return 0;
}