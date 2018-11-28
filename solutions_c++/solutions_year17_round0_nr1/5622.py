#include < stdio.h>
#include < string.h>

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t, k, i, j, l, len, f, cnt;
	char s[1005];

	scanf("%d\n", &t);
	  
	for (i = 0; i < t; i++)
	{
		scanf("%s %d\n", s, &k);

		len = strlen(s);

		cnt = 0;
		for (j = 0; j < len - k + 1; j++)
			if (s[j] == '-')
			{
				cnt++;
				for (l = j; l < j + k; l++)
					if (s[l] == '+')
						s[l] = '-';
					else
						s[l] = '+';
			}

		f = 0;
		for (j = 0; j < len; j++)
			if (s[j] == '-')
			{
				f = 1;
				break;
			}

		if (f == 1)
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		else
			printf("Case #%d: %d\n", i + 1, cnt);
	}

	return 0;
}