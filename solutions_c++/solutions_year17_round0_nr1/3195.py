#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<queue>
#include<map>
#include<functional>

using namespace std;

char str[1005];

bool flip(int st, int k)
{
	int len = strlen(str);
	int i, j;
	for (i = st, j = 0; j < k; i++, j++)
	{
		if (i >= len)
			return false;
		if (str[i] == '+')
			str[i] = '-';
		else
			str[i] = '+';
	}
	return true;
}

int main()
{
	freopen("a-large.in", "rt", stdin);
	freopen("a-large.out", "wt", stdout);
	int i, j, kase, inp, n, k, l, r;
	scanf("%d", &inp);
	for (kase = 1; kase <= inp; kase++)
	{
		scanf("%s %d", str, &k);
		int tot = 0;
		int len = strlen(str);
		for (i = 0; i < len; i++)
		{
			if (str[i] == '-')
			{
				if (flip(i, k))
				{
					tot++;
				}
				else 
				{
					tot = -1;
					break;
				}
			}
		}
		printf("Case #%d: ", kase);
		if (tot < 0)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", tot);
	}
	return 0;
}
