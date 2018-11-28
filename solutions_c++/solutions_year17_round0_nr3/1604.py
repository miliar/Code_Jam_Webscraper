#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	long long mx,mi;
	int T;
	long long n,k;
	scanf("%d",&T);
	for (int t = 1; t <= T; t ++)
	{
		scanf("%lld%lld",&n,&k);
		long long cnt1 = 1;
		long long cnt2 = 0;
		long long x1 = n;
		while (k > cnt1 + cnt2)
		{
			k -= (cnt1 + cnt2);
			long long temp1,temp2;
			if (x1 % 2 == 0)
			{
				temp1 = cnt1;
				temp2 = cnt1 + 2 * cnt2;
			}
			else 
			{
				temp1 = 2 * cnt1 + cnt2;
				temp2 = cnt2; 
			}
			x1 = x1 / 2;
			cnt1 = temp1;
			cnt2 = temp2;
		}
		if (k <= cnt1)
		{
			if (x1 % 2 == 0)
			{
				mx = x1 / 2;
				mi = mx - 1;
			}
			else 
			{
				mx = x1 / 2;
				mi = mx;
			}
		}
		else 
		{
			x1 --;
			if (x1 % 2 == 0)
			{
				mx = x1 / 2;
				mi = mx - 1;
			}
			else 
			{
				mx = x1 / 2;
				mi = mx;
			}
		}
		printf("Case #%d: %lld %lld\n",t,mx,mi);
	}
	return 0;
}