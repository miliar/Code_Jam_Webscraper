#include <iostream>
#include <cstdio>
#include <cstring>

#define maxn 1009
#define ESP 0.0000001

using namespace std;



long long k[maxn], s[maxn];
long long n, d;

int check(double mid)
{

	for(int i = 1; i <= n; i++)
	{
		double t = (double)(d - k[i]) / (1.0 * s[i]);
		if(t * mid > d)
		{
			return 0;
		}
	}
	return 1;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas++)
	{
		scanf("%lld%lld", &d, &n);
		//d *= 1000;
		for(int i = 1; i <= n; i++)
		{
			scanf("%lld%lld", &k[i], &s[i]);
			//k[i]*=1000;
			//s[i] *= 1000;
		}
		long double l = 0, r = 90000000000000;
		long double ll = 0, rr =  r;
		while(r - l > ESP)
		{
			long double mid = (r + l) / 2.0;
			ll = l;
			rr = r;
			if(check(mid))
			{
				l = mid;
			}
			else
			{
				r = mid;
			}
			if(ll == l &&  rr == r)
			{
                break;
			}
		}
		//memset(a, 0, sizeof(a));
		printf("Case #%d: ", cas);
		int z = (int)r;
		printf("%.6Lf\n", r - 0.0000005 );
	}

	return 0;
}


