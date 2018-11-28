#include <bits/stdc++.h>
using namespace std;

char num[22];

int main()
{
	int T;

	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		num[0] = '0';
		scanf("%s", num + 1);

		int l = strlen(num), ind, sind;
		for (ind = 1; ind < l; ind++)
			if (num[ind] < num[ind - 1])
				break;
		while (ind < l && num[ind] < num[ind - 1])
		{
			ind--;
			num[ind]--;
		}
		ind++;
		while (ind < l)
		{
			num[ind] = '9';
			ind++;
		}
		sind = 0;
		while (num[sind] == '0')
			sind++;
		printf("Case #%d: %s\n", t, num + sind);
	}

	return 0;
}