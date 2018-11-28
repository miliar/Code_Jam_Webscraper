#include <bits/stdc++.h>

using namespace std;

char a[1005];

int main()
{
	int tt, casos = 1;
	scanf("%d\n", &tt);

	while (tt--) 
	{
		int k;
		scanf("%s %d", a, &k);

		int ans = 0, size = strlen(a);
		for (int i = 0; i < size-k+1; ++i)
		{
			if (a[i] == '-')
			{
				++ans;
				for (int j = i; j < i+k; ++j)
					a[j] = a[j] == '-' ? '+' : '-';
			}
		}

		bool ok = true;
		for (int i = 0; i < size; ++i)
			ok &= a[i] == '+';

		printf("Case #%d: ", casos++);
		if (ok)
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}