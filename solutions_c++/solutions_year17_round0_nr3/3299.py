#include <cstdio>
#include <cassert>
#include <map>
#include <functional>
using namespace std;

#ifdef _MSC_VER
#pragma warning(disable: 4996) // Disable deprecation
#endif 

typedef long long ll;

typedef pair<ll, ll> LLPAIR;
typedef map<ll, ll, greater<ll>> GAPS;

LLPAIR Solve(ll n, ll k)
{
	GAPS gaps;
	gaps[n] = 1;

	while (!gaps.empty())
	{
		auto best = *gaps.begin();
		//if (best.first <= 0)
		//	int wdfrqw = 245;
		gaps.erase(gaps.begin());
		ll nrem = best.first - 1;
		ll s1 = nrem >> 1;
		ll s2 = nrem - s1; //bigger
		if (best.second < k && nrem > 0)
		{
			//if (!(s1 >= 0 && s2 > 0))
			//	int wfrw = 124;

			k -= best.second;
			if (s1 == s2)
			{
				gaps[s1] += 2 * best.second;
			}
			else
			{
				if (s1 > 0)
				{
					gaps[s1] += best.second;
				}
				gaps[s2] += best.second;
			}
		}
		else
		{
			return {s2, s1};
		}
	}
	return{ 0, 0 };
}

int main()
{
	//void Prob();
	//Prob();
	//return 0;

//	freopen("c.in", "r", stdin);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		ll N, K;
		scanf("%lld %lld", &N, &K);
		
		LLPAIR ans = Solve(N, K);
		printf("Case #%d: %lld %lld\n", t, ans.first, ans.second);
	}

	fclose(stdout);
	return 0;
}

void Prob()
{
	for (int t = 1; t <= 100; ++t)
	{
		ll N = ll(1e+18);
		ll K = N/t;
		LLPAIR ans = Solve(N, K);
		printf("Case #%d: %lld %lld\n", t, ans.first, ans.second);
	}
}
