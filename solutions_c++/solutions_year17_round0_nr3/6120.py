#include <bits/stdc++.h>

#define lli long long int
#define pb push_back
#define pii pair <int, int>
#define pll pair <lli, lli>
#define _F first
#define _S second
#define mset(x) memset(x, 0, sizeof(x))
#define fastio() ios_base::sync_with_stdio(0)

using namespace std;

int main()
{
	int _t;
	cin >> _t;

	for(int t=1; t <= _t; t++)
	{
		int n, k;
		cin >> n >> k;

		priority_queue < pair < int, pii > > Q;

		Q.push({n, {1, n}});

		int x = 0;
		int y = n+1;

		while(k--)
		{
			auto p = Q.top();
			Q.pop();

			int s = p.first - 1;
			x = s/2 + (s%2);
			y = s/2;

			int l = p.second.first;
			int m = l + y;
			int r = p.second.second;

			Q.push({y, {l, m-1}});
			Q.push({x, {m+1, r}});
		}

		printf("Case #%d: %d %d\n", t, x, y);
	}

	return (0-0);	
}