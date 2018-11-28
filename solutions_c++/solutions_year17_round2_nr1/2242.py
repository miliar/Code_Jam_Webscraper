#include <iostream>
#include <sstream>

using namespace std;

stringstream out;

void func()
{
	int d, n;
	cin >> d >> n;
	double longest = 0.0;
	int k, s;
	for (int i = 0; i < n; ++i)
	{
		cin >> k >> s;
		double len = (double)(d - k) / s;
		if (len > longest)
			longest = len;
	}
	printf("%.6f\n", d / longest);
}

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		printf("Case #%d: ", i);
		func();
	}
	return 0;
}