#include <bits/stdc++.h>
using namespace std;

typedef pair<long long, long long> ii;

int main()
{
	int t;
	cin >> t;

	for(int cn=1; cn<=t; cn++)
	{
		long long n,k;
		cin >> n >> k;
		k--;

		priority_queue<ii> pq;
		pq.push(ii(n,1));

		long long ans = -1;

		while(k)
		{
			long long a = pq.top().first;
			long long b = 0;
			while(pq.size() && pq.top().first==a)
			{
				b += pq.top().second;
				pq.pop();
			}

			if(b>k)
			{
				ans = a;
				break;
			}

			k -= b;

			long long na1 = (a-1)/2;
			long long na2 = a/2;
			pq.push(ii(na1,b));
			pq.push(ii(na2,b));
		}

		if(ans==-1)
			ans = pq.top().first;
		printf("Case #%d: %lld %lld\n",cn,ans/2, (ans-1)/2);
	}

	return 0;
}