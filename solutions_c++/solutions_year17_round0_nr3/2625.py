#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdio.h>
#include <string>

void solve()
{
	int c =0;
	long long n, k ;
	std::cin >> n >>k;
	std::map<long long, long long> s;
	s.insert(std::make_pair(n, 1));
	while(1)
	{
		auto it = s.rbegin();
		if(k <= it->second)
		{
			printf("%lld %lld\n", it->first/2, (it->first -1)/2);
			return;
		}
		k -= it->second;
		s[it->first/2] += it->second;
		s[(it->first -1)/2] += it->second;
		s.erase(it->first);
	}
}


int main()
{
	int t;
	std::cin >> t;
	for(int i =1; i <=t;++i)
	{
		printf("Case #%d: " , i);
		solve();
	}
	return 0;
}

