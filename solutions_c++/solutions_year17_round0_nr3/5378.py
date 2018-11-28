#include <stdio.h>
#include <set>
#include <map>
#define mn(a,b) a<b ? a:b
#define mx(a,b) a>b ? a:b
#define INF 1000000000

using namespace std;

int main()
{
	int i,j,t;
	long long n, k;
	// freopen("../test.in","r",stdin);
	// freopen("../test.out","w",stdout);
	scanf("%d",&t);
	long long tmp;
	for(int l = 1; l <= t; l++)
	{
		set <long long > s;
		set <long long >::iterator it;
		map <long long, long long> x;
		long long chk;
		long long tmp;
		scanf("%lld %lld",&n,&k);
		s.insert(n);
		k--;
		x[n] = 1;
		while(1)
		{
			it = s.end();
			it = --it;
			s.erase(it);
			chk = *it;
			tmp = x[chk];
			if(tmp > k)
			{
				break;
			}
			k -= tmp;
			if(chk%2 == 1)
			{
				s.insert(chk/2);
				x[chk/2] += 2*tmp;
			}
			else
			{
				s.insert(chk/2);
				s.insert(chk/2 - 1);
				x[chk/2] += tmp;
				x[chk/2 - 1] += tmp;
			}
		}
		if(chk%2 == 1)
		{
			printf("Case #%d: %lld %lld\n",l,chk/2,chk/2);
		}
		else
		{
			printf("Case #%d: %lld %lld\n",l,chk/2,chk/2 - 1);
		}
	}
	return 0;
}