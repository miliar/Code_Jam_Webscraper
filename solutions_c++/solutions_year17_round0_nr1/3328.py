#include <bits/stdc++.h>
#define ll long long
using namespace std;

char ch[1002];

void flip(int pos, int k)
{
	for(int i = 0; i < k; i++)
	{
		if(ch[pos + i] == '-')
		{
			ch[pos + i] = '+';
		}
		else
		{
			ch[pos + i] = '-';
		}
	}
}

bool ok(int len)
{
	for(int i = 0; i < len; i++)
	{
		if(ch[i] == '-')
		{
			return false;
		}
	}
	return true;
}

int main()
{
	freopen("0.in", "r", stdin);
	freopen("0.out", "w", stdout);

	int tc;

	scanf("%d", &tc);

	for(int t = 1; t <= tc; t++)
	{
		printf("Case #%d: ", t);
		int K;
		scanf("%s %d", ch, &K);
		
		int ans = 0;
		int len = strlen(ch);

		for(int i = 0; i + K - 1 < len; i++)
		{
			if(ch[i] == '-')
			{
				ans++;
				flip(i, K);
			}
		}
		if(ok(len))
		{
			printf("%d\n", ans);
		}
		else
		{
			printf("IMPOSSIBLE\n");
		}
	}

	return 0;
}