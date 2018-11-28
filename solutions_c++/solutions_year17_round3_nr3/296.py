#include <iostream>
#include <sstream>
#include <set>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;
const double PI = acos(-1.);


void solve()
{

	return;
}

int main()
{
	freopen("C-small-1-attempt0 (1).in", "r", stdin);
	freopen("a.out", "w+", stdout);
	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; ++t)
	{
		int n, k;
		cin >> n >> k;
		double uu;
		cin >> uu;
		ll u = round(uu * 10000);
		vector <double> vv(n);
		vector <ll> v(n);
		
		for (int i = 0; i < n; ++i)
		{
			cin >> vv[i];
			v[i] = round(vv[i] * 10000);
		}
		double res = 1.;
		bool fl = true;
		while (fl)
		{
			if (vv.size() == 0)
				break;
			fl = false;
			sort(vv.begin(), vv.end());
			double mean = uu;
			for(int i =0; i < vv.size(); ++i)
				mean += vv[i];
			mean /= vv.size();
			if (vv.back() > mean)
			{
				res *= vv.back();
				vv.pop_back();
				fl = true;
			}
			else
			{
				for (int i = 0; i < vv.size(); ++i)
					res *= mean;
			}
		}

		cout << "Case #" << t << ": ";
		printf("%.9lf\n", res);
	}
	return 0;
}