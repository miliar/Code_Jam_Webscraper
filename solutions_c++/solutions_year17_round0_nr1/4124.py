#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
using namespace std;
int T, n;
char s[1005];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int i = 1; i <= T; i++)
	{
		int cnt = 0, ok = 0;
		scanf("%s%d", s, &n);
		for(int j = 0; j < strlen(s); j++)
		{
			if(s[j] == '-' && j <= strlen(s) - n)
			{
				for(int k = 0; k < n; k++)
					if(s[j + k] == '-')s[j + k] = '+';
					else s[j + k] = '-';
				cnt++;
			}
			else if(j > strlen(s) - n && s[j] == '-')ok = 1;
		}
		if(ok)printf("Case #%d: IMPOSSIBLE\n", i);
		else printf("Case #%d: %d\n", i, cnt);

	}
	return 0;

}
