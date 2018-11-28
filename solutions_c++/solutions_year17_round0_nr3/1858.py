#include <cstdlib>
#include <cstdio>
#include <map>

using namespace std;
typedef long long LL;
LL n, k;
void Solve()
{
	scanf("%I64d%I64d", &n, &k);
	LL len1, len2, cnt1 = 0, cnt2 = 0;
	if (n & 1)
	{
		len1 = n / 2;
		len2 = 0;
		cnt1 = 2;
	}
	else
	{
		len1 = n / 2 - 1;
		len2 = n / 2;
		cnt1 = cnt2 = 1;
	}
	--k;
	if (!k)
	{
		if (len2)
			printf("%I64d %I64d\n", len2, len1);
		else
			printf("%I64d %I64d\n", len1, len1);
		return;
	}
	LL cur = 2;
	while (k > cur)
	{
		k -= cur;
		cur <<= 1;
		map<LL, LL> cnt;
		//len1
		if (len1 != 0)
		{
			if (len1 & 1)
				cnt[len1 / 2] += cnt1 * 2;
			else
			{
				cnt[len1 / 2 - 1] += cnt1;
				cnt[len1 / 2] += cnt1;
			}
		}
		//len2
		if (len2 != 0)
		{
			if (len2 & 1)
				cnt[len2 / 2] += cnt2 * 2;
			else
			{
				cnt[len2 / 2 - 1] += cnt2;
				cnt[len2 / 2] += cnt2;
			}
		}
		if (cnt.size() == 1)
		{
			len1 = cnt.begin()->first;
			len2 = 0;
			cnt1 = cnt.begin()->second;
			cnt2 = 0;
		}
		else
		{
			len1 = cnt.begin()->first;
			len2 = cnt.rbegin()->first;
			cnt1 = cnt.begin()->second;
			cnt2 = cnt.rbegin()->second;
		}
	}
	if (k <= cnt2)
	{
		if (len2 & 1) printf("%I64d %I64d\n", len2 / 2, len2 / 2);
		else if (len2 != 0) printf("%I64d %I64d\n", len2 / 2, len2 / 2 - 1);
		else puts("0 0");
	}
	else
	{
		if (len1 & 1) printf("%I64d %I64d\n", len1 / 2, len1 / 2);
		else if (len1 != 0) printf("%I64d %I64d\n", len1 / 2, len1 / 2 - 1);
		else puts("0 0");
	}
}

int T;
int main()
{
	scanf("%d", &T);
	//T = 1;
	for (int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
