#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

int a[1000], b[1000];

void solve()
{
	int n;
	scanf("%d", &n);
	int k;
	string s;
	cin >> s >> k;
	n = s.size();
	int tot = 0, ans = 0;
	for (int i = 0; i < n; ++i)
	{
		if ((tot + (s[i] == '-'))%2==1)
		{
			if (i >= n-k+1)
			{
				printf("IMPOSSIBLE\n");
				return;
			}
			a[i] = 1;
			++tot;
			++ans;
		}
		else
			a[i] = 0;
		if (i >= k-1)
			tot -= a[i-k+1];
	}
	printf("%d\n", ans);
}

int main()
{
	freopen("b.txt", "r", stdin);
	freopen("b.out", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}