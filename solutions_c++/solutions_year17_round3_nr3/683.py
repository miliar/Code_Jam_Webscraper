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
	std::multimap<double, double> d;
	double u;
	cin >> u;
	for(int i =0; i< n;++i)
	{
		double t;
		cin >> t;
		d.insert(make_pair(t, t));
	}
	auto it1 = d.begin();
	auto it2 = d.begin();
	++it2;
	int i =1;
	while(it2 != d.end())
	{
		bool b = false;
		double t;
		if(u <= i* (it2->second - it1->second))
		{
			b = true;
			t = u/i;
			u=0;
		}
		else
		{
			u -= i * (it2->second - it1->second);
			t = it2->second - it1->second;
		}
		auto it = d.begin();
		for(int j =0; j < i;++j)
		{
			it->second +=t;
			++it;
		}
		if(b)
		{
			break;
		}
		++i;
		++it1;
		++it2;
	}
	if(u >0)
	{
		auto it = d.begin();
		while(it != d.end())
		{
			it->second += u/n;
			++it;
		}
	}
	double p =1;
	auto it = d.begin();
	while(it != d.end())
	{
		p *= it->second;
		++it;
	}
	printf("%lf\n", p);

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

