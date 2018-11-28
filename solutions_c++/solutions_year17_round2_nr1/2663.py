#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <set>

#define LIMIT 1000

struct horse
{
	int pos;
	int ms;
};
typedef struct horse horse_t;

int main(int argc, char **argv)
{
	long long t, d, k, n, s;
	double slowest_horse;

	std::cin >> t;
	for(int i = 1; i <= t; ++i)
	{
		std::cin >> d >> n;
		slowest_horse = 0.0;
		for(int j = 0; j < n; ++j)
		{
			std::cin >> k >> s;
			double r = (d - k) / (double)s;
			slowest_horse = std::max(r, slowest_horse);
		}
		double result = d / slowest_horse;

		printf("Case #%d: %.6f\n", i, result);
	}

	return 0;
}
