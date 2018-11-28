#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;
void solve()
{
	double d;
	int n;
	cin >> d >> n;
	double t=0;
	for(int i=0;i < n; ++i)
	{
		double p, s;
		cin >> p>> s;
		double l = (d - p) / s;
		if(l > t)
		{
			t =l;
		}
	}
	printf("%lf\n", d/t);

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

