#include<cstdio> 
#include<cstring>

int n, k, len, use[2010];
char s[1010];

int main()
{
//	freopen("A.in", "r", stdin);
//	freopen("A.out", "w", stdout);
	scanf("%d", &n);
	for (int I = 1; I <= n; I++)
	{
		scanf("%s%d", s, &k);
		len = strlen(s);
		int temp = 0, ans = 0;
		for (int i = 0; i < len + k; i++) use[i] = 0;
		for (int i = 0; i < len; i++)
		{
			temp ^= use[i];
			if ((s[i] == '+' && !temp) || (s[i] == '-' && temp)) continue;
			temp ^= 1;
			use[i + k] = 1;
			ans++;
		}
		for (int i = len + 1; i < len + k; i++) if (use[i]) ans = -1;
		printf("Case #%d: ", I);
		if (ans == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	return 0;
}
