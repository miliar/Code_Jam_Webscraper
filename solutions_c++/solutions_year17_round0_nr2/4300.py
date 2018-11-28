#include<cstdio>
#include<cstring>

int n, len;
char s[20];

int main()
{
//	freopen("B.in", "r", stdin);
//	freopen("B.out", "w", stdout);
	scanf("%d", &n);
	for (int I = 1; I <= n; I++)
	{
		scanf("%s", s);
		len = strlen(s);
		printf("Case #%d: ", I);
		int p = 0, x = 0;
		if (len == 1)
		{
			printf("%s\n", s);
			continue;
		}
		for (int i = 1; i < len; i++) if (s[i] < s[i - 1])
		{
			p = i;
			break;
		}
		if (!p)
		{
			printf("%s\n", s);
			continue;
		}
		for (int i = p - 1; i; i--) if (s[i] - 1 >= s[i - 1])
		{
			x = i;
			break;
		}
		s[x]--;
		for (int i = x + 1; i < len; i++) s[i] = '9';
		if (s[0] == '0') printf("%s\n", s + 1);
		else printf("%s\n", s);
	}
	return 0;
}
