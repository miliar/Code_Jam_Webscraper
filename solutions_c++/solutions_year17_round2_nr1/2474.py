#include <iostream>
#include <cstdio>

using namespace std;

int main(int argc, char const *argv[])
{
	long t, cas, d, n, k, s;
	double max;

	cin >> t;
	cas = 1;

	while (cas <= t) {
		cin >> d >> n;
		max = 0;

		for (int i = 0; i < n; ++i)
		{
			cin >> k >> s;

			if (((double)(d-k))/s > max)
				max = ((double)(d-k))/s;
		}
		max = d/max;

		cout << "Case #" << cas << ": ";
		printf("%.6lf\n", max);
		cas++;

	}

	return 0;
}