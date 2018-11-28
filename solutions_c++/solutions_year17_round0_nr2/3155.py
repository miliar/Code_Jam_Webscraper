#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<queue>
#include<map>
#include<functional>

using namespace std;

char str[1005];

int main()
{
	freopen("b-large.in", "rt", stdin);
	freopen("b-large.out", "wt", stdout);
	int i, j, kase, inp, n, k, l, r, len;
	scanf("%d", &inp);
	for (kase = 1; kase <= inp; kase++)
	{
		scanf("%s", str, &k);
		int tot = 0;
		len = strlen(str);
		bool flag = false;
		for (i = 1; i < len; i++)
		{
			if (flag)
			{
				str[i] = '9';
				continue;
			}
			if (str[i] < str[i - 1])
			{
				for (j = i; j > 0; j--)
				{
					if (str[j] >= str[j - 1])
						break;
					str[j - 1]--;
					str[j] = '9';
				}
				flag = true;
			}

		}
		printf("Case #%d: ", kase);
		flag = false;
		for (i = 0; i < len; i++)
		{
			if (flag)
			{
				printf("%c", str[i]);
				continue;
			}
			if (str[i] > '0')
			{
				printf("%c", str[i]);
				flag = true;
			}
		}
		printf("\n");
	}
	return 0;
}
