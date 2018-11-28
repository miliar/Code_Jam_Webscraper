#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("data.in","r",stdin),freopen("data.out","w",stdout);
	int t;
	scanf("%d", &t);
	for(int i = 1;i <= t;i ++)
	{
		printf("Case #%d: ", i);
		static char s[100];
		static char ans[100];
		scanf("%s", s);
		int n = strlen(s);
		for(int i = 0;i < n;i ++)
			for(char ch = '9';ch >= '0';ch --)
			{
				for(int p = i;p < n;p ++) ans[p] = ch;
				bool ok = 1;
				for(int p = 0;p < n;p ++)
					if (ans[p] > s[p]) {ok = 0;break;} else
						if (ans[p] < s[p]) break;
				if (!ok) continue;
				break;
			}
		for(int i = 0;i < n;i ++)
			if (ans[i] != '0')
			{
				for(int j = i;j < n;j ++) printf("%c", ans[j]);
				break;
			}
		printf("\n");
	}
	return 0;
}
