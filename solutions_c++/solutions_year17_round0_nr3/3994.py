#include <cstdio>
#include <algorithm>
#include <vector>

using std::vector;
using std::make_heap;
using std::pop_heap;
using std::push_heap;
using std::swap;
typedef long long int ll;

int cmp(const ll a, const ll b)
{
	return a < b;
}


int main()
{
	int T;
	scanf("%d", &T);
	int cnt = 1;
	while(T--)
	{
		ll N, k;
		scanf("%lld%lld", &N, &k);
		vector<ll> v;
		v.push_back(N);
		make_heap(v.begin(), v.end(), cmp);
		for(ll i = 0; i < k; i++)
		{
			ll a = v.front();
			pop_heap(v.begin(), v.end(), cmp);
			v.pop_back();
			a --;
			long long int y = a/2, x = a-(a/2);
			if(i == k-1)
			{
				printf("Case #%d: %lld %lld\n", cnt, x, y);
			}
			if(y > 0)
			{
				v.push_back(y);
				push_heap (v.begin(),v.end(), cmp);
			}
			if(x > 0)
			{
				v.push_back(x);
				push_heap (v.begin(),v.end(), cmp);
			}
		}
		cnt++;
	}


	return 0;
}