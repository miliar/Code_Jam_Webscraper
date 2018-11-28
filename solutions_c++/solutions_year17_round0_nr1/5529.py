#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int MAXN = 1005;
int t, k;
char s[MAXN];
int a[MAXN];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%s%d", s+1, &k);
		int n = strlen(s+1);
		a[0] = 0;
		if (s[1] == '+') a[1] = 0;
		else a[1] = 1;
		for (int i = 2; i <= n; i++)
		{
			if (s[i] != s[i-1]) a[i] = 1;
			else a[i] = 0;
		}
		int cnt = 0;
		for (int i = 1; i <= n-k+1; i++)
		{
			if (a[i])
			{
				a[i] ^= 1;
				a[i+k] ^= 1;
				cnt++;
			}
		}
		bool flag = 1;
		for (int i = n-k+1; i <= n; i++)
			if (a[i])
				flag = 0;
		if (flag) printf("%d\n", cnt);
		else puts("IMPOSSIBLE"); 
				
	}
} 
