#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdio.h>
#include <string>

long long find_n(long long n, long long c, long long d, long long b)
{
	long long r = c;
	for(int i =d; i >0;--i)
	{
		long long t = c + i * b;
		if(t <= n)
			r = std::max(r, find_n(n, t, i, b*10));
	}
	return r;
}
void solve()
{
	long long n;
	long long r =0;
	std::cin >> n;
	int s=9;
	if (n <s)
		s = n;
	for(int i =1; i <=s; ++i)
	{
		r = std::max(r, find_n(n, i, i, 10));
	}
	printf("%lld\n",r);
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

