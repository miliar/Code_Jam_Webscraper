#include <stdio.h>
#include <string.h>

const int MAX_LEN = 20;

char inp[MAX_LEN];

void process()
{
	int i, j, k, len;

	len = strlen(inp);
	for (i = 1; i < len; i++)
	{
		if (inp[i - 1] > inp[i])
			break;
	}
	if (i >= len)
	{
		printf("%s\n", inp);
		return;
	}
	if (inp[i - 1] >= '2')
	{
		for (j = i - 1; j > 0; j--)
		{
			if (inp[j - 1] < inp[j])
				break;
		}
		inp[j]--;
		for (i = j + 1; i < len; i++)
			inp[i] = '9';
		printf("%s\n", inp);
		return;
	}
	for (i = 0; i < len - 1; i++)
		printf("9");
	printf("\n");
}

int main()
{
	int t, i;

	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		scanf("%s", inp);
		printf("Case #%d: ", i);
		process();
	}
}