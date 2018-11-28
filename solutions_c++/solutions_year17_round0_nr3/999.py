#include<iostream>
#include<cstdio>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cstring>
#include<string>
#include<vector>
#include<iomanip>
#include<unordered_set>
#include<unordered_map>
#include<cmath>
#include<list>
#include<bitset>
using namespace std;

#define ull unsigned long long
#define ll long long
#define lson l,mid,id<<1
#define rson mid+1,r,id<<1|1

typedef pair<int, int>pii;
typedef pair<ll, ll>pll;
typedef pair<double, double>pdd;
const double eps = 1e-6;
const int MAXN = 100005;
const int MAXM = 5005;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const int INF = 0x3f3f3f3f;
const double FINF = 1e18;
const ll MOD = 1000000007;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t, cas = 0, ans;
	ll n, k;
	scanf("%d", &t);
	map<ll, ll>mp;
	while (t--)
	{
		mp.clear();
		ll ans1, ans2;
		scanf("%lld%lld", &n, &k); mp[n] = 1;
		for (auto ite = mp.rbegin(); ite != mp.rend(); ++ite)
		{
			//if (ite->second == 0)continue;
			if (k <= ite->second)
			{
				ans1 = ite->first / 2;
				if (ite->first % 2 == 0)ans2 = ans1 - 1;
				else ans2 = ans1;
				printf("Case #%d: %lld %lld\n", ++cas, ans1, ans2);
				break;
			}
			else
			{
				if (ite->first == 1)
				{
					printf("Case #%d: 0 0\n", ++cas);
					break;
				}
				else
				{
					mp[ite->first / 2] += ite->second;
					if (ite->first % 2 == 0)mp[ite->first / 2 - 1] += ite->second;
					else mp[ite->first / 2] += ite->second;
					k -= ite->second;
					mp[ite->first] = 0;
				}
			}
		}
	}
}
/*
635 488
317 237
*/