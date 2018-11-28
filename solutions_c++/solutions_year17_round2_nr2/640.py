#include <bits/stdc++.h>
using namespace std;

char s[1005];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	int n;
	int r, o, y, g, b, v;
	scanf("%d", &T);
	for (int z = 1; z <= T; z++)
	{
		memset(s, 0, sizeof(s));
		scanf("%d", &n);
		scanf("%d %d %d %d %d %d", &r, &o, &y, &g, &b, &v);
		string ord = "RYB";
		int num[3] = {r, y, b};
		bool ok = true;
		for (int i = 0; i < 3; i++)
		{
			if (num[i]*2 > n)
				ok = false;
		}
		if (!ok)
		{
			printf("Case #%d: IMPOSSIBLE\n", z);
			continue;
		}
		for (int i = 0; i < 3; i++)
			for (int j = i; j < 3; j++)
			{
				if (num[i] < num[j])
				{
					swap(num[i], num[j]);
					swap(ord[i], ord[j]);
				}
			}
		for (int i = 0; i < num[0]; i++)
		{
			s[2*i] = ord[0];
		}
		int j = n-1;
		for (int i = 0; i < num[1]; i++)
		{
			while (s[j] != 0)
				j--;
			s[j] = ord[1];
			j -= 2;
		}
		for (int i = 0; i < n; i++)
			if (s[i] == 0)
				s[i] = ord[2];
		printf("Case #%d: %s\n", z, s);
	}
}