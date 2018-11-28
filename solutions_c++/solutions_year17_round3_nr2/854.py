#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdio.h>
#include <string>
#include <vector>
#include <set>
#include <math.h>
#include <tuple>
using namespace std;
void solve()
{
	std::map<int, std::tuple<int, int, bool> > d;
	int a, b;
	cin >> a >> b;
	for(int i=0; i < a;++i)
	{
		int t, q;
		cin >> t >> q;
		d.insert(make_pair(t, make_tuple(t, q, true)));
	}
	for(int i=0; i < b;++i)
	{
		int t, q;
		cin >> t >> q;
		d.insert(make_pair(t, make_tuple(t, q, false)));
	}

	auto it1 = d.begin();
	auto it2 = d.begin();
	++it2;
	while(it2 != d.end())
	{
		int s1; int e1; bool u1;
		int s2; int e2; bool u2;
		tie(s1, e1, u1) = it1->second;
		tie(s2, e2, u2) = it2->second;
		if(u1 == u2)
		{
			if(e2 - s1 <= 720)
			{
				it1->second = make_tuple(s1, e2, u1);
				auto it = it2;
				++it2;
				d.erase(it);
			}
			else
			{
				++it1;
				++it2;
			}
		}
		else
		{
			++it1;
			++it2;
		}
	}
	it1 = d.begin();
	auto it3 = d.rbegin();
	if(d.size()>=2)
	{
		int s1; int e1; bool u1;
		int s2; int e2; bool u2;
		tie(s1, e1, u1) = it1->second;
		tie(s2, e2, u2) = it3->second;
		if(u1 == u2)
		{
			if((1440 + e1 - s2) <= 720)
			{
				it3->second = make_tuple(s2 - 1440, e1, u1);
				d.erase(it1);
			}
		}
	}
	int tb =0, tf=0;
	auto it = d.begin();
	while(it != d.end())
	{
		if(get<2>(it->second))
		{
			tb ++;
		}
		else
		{
			tf++;
		}
		++it;
	}
	if(tb < tf)
	{
		tb = tf;
	}
	printf("%d\n", tb * 2);

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

