#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int t, d, n;

	cin >> t;
	for(int idxCase = 0; idxCase < t; idxCase++)
	{
		int n;
		double d, k, s;
		double minResult = 0.0;
		cin >> d >> n;

		for(int idxHorse = 0; idxHorse < n; idxHorse++)
		{
			cin >> k >> s;
			if(minResult > d / ((d - k) / s) || idxHorse == 0)
			{
				minResult = d / ((d - k) / s);
			}
		}
		cout << setprecision(6) << fixed;
		cout << "Case #" << idxCase + 1 << ": " << minResult << endl;
	}

		return 0;
}

/*
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
*/