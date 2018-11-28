#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<queue>
#include<stack>
#include<cfloat>
#include<cmath>
#include<algorithm>
#define M 1005 
using namespace std;

long long int_pow(int base, int exp)
{
    long long result = 1;
    while (exp)
    {
        if (exp & 1)
           result *= base;
        exp /= 2;
        base *= base;
    }
    return result;
}

int main(void)
{
	int T;
	cin >> T;
	for (int z = 1; z <= T; ++z)
	{
		int k, n;
		cin >> n >> k;
		vector<pair<double, double> > p;
		for (int i = 0; i < n; ++i)
		{
			double r, h;
			cin >> r >> h;
			p.push_back(make_pair(r, h)); 
		} 
		sort(p.begin(), p.end()); 
		double  ans = 0;
		for (int i = k-1; i < n; ++i)
		{
			double tmp = M_PI * p[i].first * p[i].first + 2 * M_PI * p[i].first * p[i].second;
			vector<double> v;
			for (int j = 0; j <i; ++j)
				v.push_back(2*M_PI*p[j].first*p[j].second);
			sort(v.begin(), v.end());
			for (int j = 1; j < k; ++j)
				tmp += v[v.size() - j];
			ans = max(ans, tmp);
		}
		printf("Case #%d: %.9lf\n", z, ans);
	}
	return 0;
}

