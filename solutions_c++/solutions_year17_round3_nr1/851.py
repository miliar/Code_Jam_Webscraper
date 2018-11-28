#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdio.h>
#include <string>
#include <vector>
#include <set>
#include <math.h>

using namespace std;
void solve()
{
	int n,k;
	cin >> n >>k;
	std::multimap<long long , std::set<long long>::iterator> v;
	std::multiset<long long > w;

	for(int i =0; i < n;++i)
	{
		long long a, b;
		cin >> a >> b;
		auto it = w.insert(2*a *b);
		v.insert(make_pair(a*a, it));
	}

	long long max =0;
	while(v.size() >=k)
	{
		auto it = v.rbegin();
		long long t = it->first + *(it->second);
		w.erase(it->second);
		++it;
		v.erase(it.base());
		auto g = w.rbegin();
		for(int i =0; i < (k -1);++i)
		{
			t += *(g);
			++g;
		}
		if(max < t)
		{
			max  =t;
		}
	}

	
	printf("%lf\n", ((double)max) * M_PI);

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

