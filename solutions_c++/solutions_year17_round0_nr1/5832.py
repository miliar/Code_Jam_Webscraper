#include <stdio.h>
#include <string.h>

int k, ans;
const int MAX_INP = 1050;

char inp[MAX_INP];

void process()
{
	int d[MAX_INP], i, j, len, cnt = 0;

	ans = -1;
	len = strlen(inp);
	for (i = 0; i < len; i++)
	{
		if (inp[i] == '-') d[i] = 0;
		else d[i] = 1;
	}
	for (i = 0; i < len - k + 1; i++)
	{
		if (d[i] == 0)
		{
			for (j = 0; j < k; j++)
				d[i + j] ^= 1;
			cnt++;
		}
	}
	for (i = 0; i < len; i++)
		if (d[i] == 0) break;

	if (i < len) return;
	ans = cnt;
}

int main()
{
	int t, i;

	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		scanf("%s %d", inp, &k);
		process();
		printf("Case #%d: ", i);
		if (ans == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	return 0;
}