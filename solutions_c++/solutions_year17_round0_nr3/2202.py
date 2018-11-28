#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
int main()
{
	ios::sync_with_stdio(0);
	int T;
	cin>>T;
		int tc = 1;
	while (T--)
	{
		long long N, K;
		cin>>N>>K;
		queue<long long> pq;
		pq.push(N);
		unordered_map<long long, long long> m;
		long long ax, bx;
		m[N] = 1;
		while (true)
		{
			long long u = pq.front(); pq.pop();
//			cerr<<u<<' '<<m[u]<<' '<<K<<'\n';
			if (K > m[u])
			{
				K -= m[u];
				
				if (u % 2 == 1)
				{
					ax = bx = u/2;
				}
				else
				{
					ax = u/2;
					bx = ax-1;
				}

				if (m[ax] == 0)
					pq.push(ax);
				if (m[bx] == 0)
					pq.push(bx);
				
//				cerr<<ax<<' '<<bx<<'\n';

				m[ax] += m[u];
				m[bx] += m[u];
				
				m[u] = 0;			
			}
			else
			{
				if (u % 2 == 1)
				{
					ax = bx = u/2;
				}
				else
				{
					ax = u/2;
					bx = ax-1;
				}
				cout<<"Case #"<<tc++<<": "<<ax<<" "<<bx<<'\n';
				break;				
			}
		}
	}	
}