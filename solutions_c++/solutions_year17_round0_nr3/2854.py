#include "bits/stdc++.h"

using namespace std;
typedef pair<long long, long long> p;
p solve()
{
	long long N, K;
	scanf("%lld%lld",&N,&K);
//	K--;
	map<long long, long long int> mp;
	mp[N] = 1;
	map<long long, long long>::iterator it;
	while(1)
	{
		it = mp.end();
		it--;
		long long length = it->first;
		long long number = it->second;
		if(K <= number)
		{
			return p((length-1)/2, length/2);
		}
		K -= number;
		mp.erase(it);
		length--;
		mp[length/2] += it->second;
		mp[length/2 + length%2] += it->second;
	}
}

int main()
{
	int T,testCase;
	scanf("%d",&T);
	testCase = T;
	while(T--)
	{
		p cur = solve();
		printf("Case #%d: %lld %lld\n",testCase - T, cur.second, cur.first);
	}
	return 0;
}