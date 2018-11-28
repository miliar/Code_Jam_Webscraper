#include<stdio.h>
#include<string.h>

char func(char x)
{
	if(x == '+')
		return '-';
	return '+';
}

main()
{
	int i, j, k, N, T, K, bol, cont;
	char msg[1001];
	scanf("%d%*c", &T);
	for(k = 1; k <= T; k++)
	{
		cont = 0;
		scanf("%s %d%*c", msg, &K);
		N = strlen(msg);
		for(i = 0; i <= N - K; i++)
		{
			if(msg[i] == '-')
			{
				cont++;
				for(j = i; j < i + K; j++)
					msg[j] = func(msg[j]);
			}
		}
		bol = 1;
		for(; i < N; i++)
			bol &= msg[i] == '+';
		if(bol)
			printf("Case #%d: %d\n", k, cont);
		else
			printf("Case #%d: IMPOSSIBLE\n", k);
	}
	return 0;
}
