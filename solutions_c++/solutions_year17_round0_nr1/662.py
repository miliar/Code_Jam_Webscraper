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
		static char s[10005];
		int k,ans = 0;
		scanf("%s%d", s, &k);
		int n = strlen(s);
		bool ok = 1;
		for(int i = 0;i < n;i ++)
			if (s[i] == '-')
			{
				if (i + k - 1 >= n) {ok = 0;break;}
				++ ans;
				for(int j = 0;j < k;j ++)
				{
					int ty = (s[i + j] == '-');
					ty ^= 1;
					if (ty) s[i + j] = '-'; else s[i + j] = '+';
				}
			}
		if (!ok) printf("IMPOSSIBLE\n"); else printf("%d\n", ans);
	}
	return 0;
}
