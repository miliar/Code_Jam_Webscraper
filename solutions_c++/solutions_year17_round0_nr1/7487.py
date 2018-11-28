#include<cstdio>

char txt[2000];

int main()
{
	int T; scanf("%d", &T);
	for (int _ = 0; _ < T; ++_)
	{
		int K;
		scanf("%s %d", txt, &K);
		int c = 0;
		for (int i = 0; txt[i] && c >= 0; ++i)
		{
			if (txt[i] == '-')
			{
				++c;
				for (int j = 0; j < K; ++j)
				{
					if (!txt[i+j]) {
						c = -1; break;
					}
					txt[i+j] = (txt[i+j] == '-') ? '+' : '-';
				}
			}
		}
		printf("Case #%d: ", _+1);
		if (c < 0)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", c);
	}
	return 0;
}
