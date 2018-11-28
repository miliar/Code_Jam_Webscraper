#include < stdio.h>
#include < string.h>

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	long long t, i, j, l, len;
	char s[30];

	scanf("%lli\n", &t);

	for (i = 0; i < t; i++)
	{
		scanf("%s\n", s);

		len = strlen(s);

		for (j = len - 2; j >= 0; j--)
			if (s[j] > s[j + 1])
			{
				s[j]--;

				for (l = j + 1; l < len; l++)
					s[l] = '9';
			}

		if (s[0] == '0')
		{
			printf("Case #%lli: ", i + 1);

			for (j = 0; j < len - 1; j++)
				printf("9");

			printf("\n");
		}
		else
			printf("Case #%lli: %s\n", i + 1, s);
	}

	return 0;
}