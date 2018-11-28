#include<iostream>
#include<vector>
#include<iomanip>
#include<algorithm>
using namespace std;
vector<double>s;
int main()
{
	int t;
	cin >> t;
	for (int ii = 1; ii <= t; ++ii)
	{
		s.clear();
		long long d, n, ki, si;
		cin >> d >> n;
		for (int i = 1; i <= n; ++i)
		{
			cin >> ki >> si;
			s.push_back((double)(d - ki) / si);
		}
		sort(s.begin(), s.end());
		cout << "Case #" << ii << ": ";
		cout << fixed << setprecision(6) << (double)d / s.back() << endl;
	}
}