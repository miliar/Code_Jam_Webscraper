#include<cstdio>
#include<queue>
#include<algorithm>
#include<map>
using namespace std;
typedef long long ll;
int main()
{
	int t, tc;
	scanf("%d", &tc);
	for (t = 1; t <= tc; t++)
	{
		ll n, m;
		scanf("%lld%lld", &n, &m);
		priority_queue<ll> q;
		q.push(n);
		map<ll, ll> d;
		d[n] = 1;
		printf("Case #%d: ", t);
		while (m)
		{
			ll k = q.top(); q.pop();
			ll cnt = d[k]; d.erase(k);
			if (cnt >= m)
			{
				printf("%lld %lld\n", k / 2, (k - 1) / 2);
				break;
			}
			m -= cnt;
			if (k / 2 > 0)
			{
				if (d.find(k / 2) == d.end())
				{
					d[k / 2] = cnt;
					q.push(k / 2);
				}
				else d[k / 2] += cnt;
			}
			if ((k - 1) / 2 > 0)
			{
				if (d.find((k - 1) / 2) == d.end())
				{
					d[(k - 1) / 2] = cnt;
					q.push((k - 1) / 2);
				}
				else d[(k - 1) / 2] += cnt;
			}
		}
	}
	return 0;
}
