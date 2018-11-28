#include <stdio.h>
#include <string.h>

int d[100];

int main()
{
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		int N, K;
		scanf("%d%d", &N, &K);

		int count = 0;
		for (int i = K; i > 1; i /= 2)
		{
			d[count++] = i;
		}

		int ans = N;
		for (int i = 0; i < count; i++)
		{
			if (d[i] % 2)
			{
				ans = (ans - 1) / 2;
			}
			else
			{
				ans = ans / 2;
			}
		}

		if (ans == 0) ans = 1;

		printf("Case #%d: %d %d\n", t, ans / 2, (ans - 1) / 2);
	}

	return 0;
}