#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef long long ll;
ll h[1010];
ld memo[1010][1010];
ll done[1010][1010];
ll upto, t, n, k;
ll r[1010];
ld pi;
ld dp(int a, int left)
{
	if (a == n) return 0;
	if (done[a][left] == upto) return memo[a][left];
	done[a][left] = upto;
	ld ans = dp(a+1, left);
	if (left == 1)
	{
		ans = max(ans, 2.0*pi*(ld)r[a]*(ld)h[a] + pi*(ld)r[a]*(ld)r[a]);
	}
	else
	{
		ans = max(ans, 2.0*pi*(ld)r[a]*(ld)h[a] + dp(a+1, left-1)); 
	}
	return memo[a][left] = ans;
}
int main()
{
	pi = 3.141592653589793;
	scanf("%lld", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%lld%lld", &n, &k);
		vector<pair<ll, ll> > inp;
		for (int i = 0; i < n; i++)
		{
			scanf("%lld%lld", &r[i], &h[i]);
			inp.push_back(make_pair(r[i], h[i]));
		}
		sort(inp.begin(), inp.end());
		for (int i = 0; i < inp.size(); i++)
		{
			h[i] = inp[i].second;
			r[i] = inp[i].first;
		}
		upto++;
		printf("Case #%d: %Lf\n", i, dp(0, k));
	}

}