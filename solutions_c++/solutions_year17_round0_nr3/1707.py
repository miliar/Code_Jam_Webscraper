#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
const int N = 20010;
typedef long long ll;
using namespace std;
typedef long long ll;
map<ll, ll>m;
priority_queue<ll> q;
int main()
{
	ll n, k;
	ll T, i1 = 1;
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%lld", &T);
	while (T--)
	{
		m.clear();
		scanf("%lld%lld", &n, &k); k--;
		while (!q.empty())
			q.pop();
		ll now=n;
		q.push(now);
		m[now] = 1;
		while (k != 0)
		{
			now = q.top(); q.pop();
			ll tmp = m[now];
			if (k >= m[now])
			{
				k -= tmp;
				if ((now - 1) % 2 == 0)
				{
					now = (now - 1) / 2;
					tmp *= 2;
					if (m[now] == 0)
						q.push(now);
					m[now] += tmp;
				}
				else
				{
					now = (now - 1) / 2;
					if (m[now] == 0)
						q.push(now);
					m[now] += tmp;
					now++;
					if (m[now] == 0)
						q.push(now);
					m[now] += tmp;
				}
			}
			else
			{
				k = 0;
				q.push(now);
			}

		}
		printf("Case #%lld: ", i1++);
		if (q.empty())
		{
			printf("0 0\n");
		}
		else
		{
			ll len = q.top();
			printf("%lld %lld\n", (len) / 2, (len - 1) / 2);
		}
	}
	return 0;
}