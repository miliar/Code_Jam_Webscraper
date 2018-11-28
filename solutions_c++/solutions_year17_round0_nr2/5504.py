#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define LL long long
int t;
LL n;
int dig[25], len;
void solve()
{
	len = 0;
	while (n)
	{
		dig[++len] = n%10;
		n /= 10;
	}
}
int main()
{
//	freopen("B-large.in","r", stdin);
//	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		scanf("%lld", &n);
		solve();
//		cout << len <<endl;
		for (int i = len-1; i >= 1; i--)
		{
			if (dig[i] < dig[i+1])
			{
				dig[i+1]--;
				for (int j = i+1; j+1 <= len && dig[j] < dig[j+1]; j++)
				{
					dig[j] = 9;
					dig[j+1]--;
				}
				for (int j = i; j >= 1; j--)
				{
					dig[j] = 9;
				}
				break;
			}
		}
		while (len&&!dig[len]) len--;
//		cout << len << endl;
		printf("Case #%d: ", tt);
		for (int i = len; i >= 1; i--)
		{
			printf("%d", dig[i]);
		}
		puts("");
	}
}
/*
838
302
551
815
6
*/
