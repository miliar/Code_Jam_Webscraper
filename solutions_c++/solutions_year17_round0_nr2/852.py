#include <bits/stdc++.h>
using namespace std;
const int N = 2010;
typedef long long ll;
int mod = 1000000007;
char s[22];
int num[22];
void run()
{
	int len = 0;
	scanf("%s", s);
	for (int i = 0; s[i]; i++, len++)
		num[i] = s[i] - '0';
	int i = 1, n = len;

	num[len] = 9;
	while (i <= len)
	{
		if (num[i] < num[i-1])
		{
			num[i] = 9;
			int left = -1;
			for (int j = i - 1; j >= 0 && left; j--)
			{
				if (num[j] + left >= 0)
				{
					num[j] += left;
					left = 0;
				}else
					num[j] = 9;
			}
			for (int j = i; j < len; j++)
				num[j] = 9;
			len = i;
			i = 1;
			continue;
		}
		i++;
	}
	i = 0;
	while (i < n - 1 && num[i] == 0)i++;

	for (; i < n; i++)
		printf("%d", num[i]);
	puts("");
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cas = 1;
	scanf("%d", &T);
	 
	while (T--)
	{ 
		printf("Case #%d: ", cas++);
		run();
	}
    return 0;
}