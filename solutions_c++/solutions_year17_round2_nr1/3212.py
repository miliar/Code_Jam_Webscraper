#include <bits/stdc++.h>
using namespace std;
const int maxn = int(1e4) + 10;
vector<pair<long long,long long>>arr;
long long t, d, n, i, j, k,a,b;
long double men;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("sal1big2.out", "w", stdout);
	int cas = 0;
	scanf("%lld",&t);
	while (t--)
	{
		arr.clear();
		scanf("%lld%lld", &d, &n);
		for(i=0;i<n;i++)
		{ 
			scanf("%lld%lld",&a,&b);
			arr.push_back({ a,b });
		}
		men = (long double)(d - arr[0].first);
		men = (men) / (1.0*arr[0].second);
		for (i = 1; i < n; i++)
		men = max(men, (long double)(d - arr[i].first) / (1.0*arr[i].second));
		printf("Case #%d: %lf\n", ++cas,1.0*d/men);
	}
}