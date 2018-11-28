#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdio.h>
#include <string>
#include <vector>
#include <tuple>
#include <algorithm>
#include <string>

using namespace std;

std::vector<double> d;
std::vector<pair<double, double> > val;
double find_ans(double s, double r, int i)
{
	++i;
	if(i == d.size())
	{
		return 0;
	}
	if(r <d[i])
	{
		return d[i]/val[i].second + find_ans(val[i].second, val[i].first - d[i], i);
	}
	return min(d[i]/val[i].second + find_ans(val[i].second, val[i].first - d[i], i), d[i]/s  + find_ans(s, r- d[i], i));
}
void solve()
{
	d.clear();
	val.clear();
	int n, q;
	cin >> n >> q;
	for(int i=0; i< n;++i)
	{
		double e,s;
		cin >> e >> s;
		val.push_back(make_pair(e, s));
	}
	for(int i =0; i < n;++i)
	{
		for(int j=0; j < n;++j)
		{
			double t;
			cin >>t;
			if((i+1)==j)
			{
				d.push_back(t);
			}
		}
	}
	for(int i =0; i < q;++i)
	{
		int t;
		cin >> t >>t;
	}

	printf("%lf\n", d[0]/val[0].second + find_ans(val[0].second, val[0].first -d[0], 0));
		

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

