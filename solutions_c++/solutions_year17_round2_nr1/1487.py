#include <iostream>
#include <vector>
#include <cstdio>
#include <limits>

using namespace std;

typedef pair <long, long> pii;

#define y first
#define x second

double solve(long d, vector <pii> h)
{
	double s = numeric_limits<double>::infinity();
	for (auto &k : h)
		s = min(s, double(d * k.x) / double(d - k.y));

	return s;
}

int main()
{
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++)
	{
		long d, n;
		cin >> d >> n;

		vector <pii> h(n);
		for (auto &k : h)
			cin >> k.y >> k.x;

		printf("Case #%d: %f\n", z, solve(d, h));
	}

	return 0;
}
