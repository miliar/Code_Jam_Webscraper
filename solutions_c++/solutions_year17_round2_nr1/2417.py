#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;
#define FX(x) fixed << setprecision((x))

int main()
{
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		long long n, d;
		cin >> d >> n;
		double result = - 1.0;

		for (int i = 0; i < n; ++i)
		{
			long long k, s;
			cin >> k >> s;
			double mv = ((double) d * (double) s) / ((double) d - (double) k);
			if (result < 0.0)
				result = mv;
			result = min(result, mv);
		}

		cout << "Case #" << test + 1 << ": " << FX(6) << result << endl;

	}
}