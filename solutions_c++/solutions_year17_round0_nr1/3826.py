#include <stdio.h>
#include <memory.h>
#include <string.h>

char S[1001];
int d[1001];

int main()
{
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		int K, N;
		scanf("%s%d", S, &K);
		memset(d, 0, K);
		N = strlen(S);

		for (int i = 0; i < N; i++)
		{
			if (S[i] == '+') d[i + 1] = d[i];
			else d[i + 1] = -1;
			if (i > N - K) continue;
			if (S[i] == '-')
			{
				for (int j = 0; j < K; j++)
				{
					S[i + j] = S[i + j] == '-' ? '+' : '-';
				}
				d[i + 1] = d[i] + 1;
			}
		}

		printf("Case #%d: ", t);
		if (d[N] == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", d[N]);
	}

	return 0;
}