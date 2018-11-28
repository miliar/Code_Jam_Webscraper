#include<cstdio>
#include <algorithm>
#include <queue>
using namespace std;
int t,i,j,v;
long long n,k,l,r,ess;
priority_queue<long long>cola;
int main()
{
	freopen("C-small-1-attempt2.in", "r", stdin);
	freopen("C-small-1-attempt2.out", "w", stdout);
	scanf("%d", &t);
	while (t--)
	{
		v++;
		scanf("%lld",&n);
		scanf("%lld",&k);
		cola.push(n);
		while (k--)
		{
			ess = cola.top();
			cola.pop();
			r = ess / 2;
			l = ess - r - 1;
			if (r)
				cola.push(r);
			if (l)
				cola.push(l);
		}
		printf("Case #%d: %lld %lld\n",v,max(l,r),min(l,r));
		while (!cola.empty())
			cola.pop();
	}
}