#include <stdio.h>
#include <string.h>
int T, N, len;
char in[20];
// len 개수만큼

int check()
{
	int ret = -1;
	for (int i = 0; i < len - 1; ++i)
	{
		if (in[i] > in[i + 1])
		{
			ret = i;
			break;
		}
	}
	return ret;
}

void modify(int n)
{
	in[n]--;
	for (int i = n + 1; i < len; ++i)
	{
		in[i] = '9';
	}
}

void solve()
{
	int num = check();
	while (num != -1)
	{
		modify(num);
		num = check();
	}
}

int main()
{
	//freopen("B-large.in", "rt", stdin);
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc)
	{
		scanf("%s", in);
		len = strlen(in);
		solve();
		printf("Case #%d: ", tc);
		for (int i = 0; i < len; ++i)
			if (in[i] != '0')
				printf("%c", in[i]);
		printf("\n");
	}
	return 0;
}