
#define _CRT_SECURE_NO_WARNINGS
#include<vector>
#include<iostream>
#include<algorithm>
#include<iomanip>

using namespace std;

bool f(vector<pair<long long int, long long int> > &v, long double m, long long int dist)
{
	long double t, min = 1e18;
	for (int i = 0; i < v.size(); ++i)
	{
		t = v[i].first / (m - v[i].second);
		if (t >= 0 && t < min)
		{
			min = t;
		}
	}
	long double res = min*m + 1e-8;
	if ( res > dist)
		return true;
	return false;
}

int main()
{
	freopen("a.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int testNum = 0; testNum < test; ++testNum)
	{
		long long int d, n;
		cin >> d >> n;
		vector<pair<long long int, long long int> > horses(n, make_pair(0,0));
		for (int i = 0; i < n; ++i)
		{
			cin >> horses[i].first >> horses[i].second;
		}

		long double l = 0, r = 1e18, m;
		//while (r - l > 1)
		for(int acc=0; acc < 100; ++acc)
		//while((r-l) > 1e-8)
		{
			m = l + (r - l) / 2;
			if (f(horses,m,d))
				l = m;
			else
				r = m;
		}
		cout << "Case #" << testNum + 1 << ": " << setprecision(7) << fixed << l << endl;
	}
	return 0;
}