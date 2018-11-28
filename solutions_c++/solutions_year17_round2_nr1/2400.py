#include <iostream>
#include <vector>
#include <list>
#include <utility>
#include <queue>
#include <functional>

using namespace std;


int main()
{
	long long t;
	vector<double> ans;
	cin >> t;
	for (long long i = 0; i < t; i++)
	{
		long long D, N;
		double mi = INFINITY;
		cin >> D >> N;
		for (long long i = 0; i < N; i++)
		{
			long long k, s;
			cin >> k >> s;
			double a = (double)D*s/(D - k);
			mi = min(a, mi);
		}
		ans.push_back(mi);
	}
	for (long long i = 0; i < ans.size(); i++)
	{
		cout << "Case #" << i + 1 << ": ";
		printf("%.6lf\n", ans[i]);
	}
	return 0;
}
