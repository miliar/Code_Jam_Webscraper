#include <iostream>
#include <string>
#include <queue>

using namespace std;

typedef unsigned long long int ull;

void stall_spacings(ull & n, ull & k, ull & l, ull & r)
{
	ull one = 1;
	ull minus_ones = 0;
	ull acc_stalls = 0;
	ull level_stalls = 1;

	

	while (true)
	{
		acc_stalls += level_stalls - minus_ones;
		if (acc_stalls >= k)
		{
			l = (n > 1) ? ((n - 1) >> 1) : 0;
			r = n >> 1;
			return;
		}

		acc_stalls += minus_ones;
		if (acc_stalls >= k)
		{
			l = (n > 2) ? ((n - 2) >> 1) : 0;
			r = (n > 1) ? ((n - 1) >> 1) : 0;
			return;
		}

		if (!(n & one))
		{
			minus_ones += level_stalls;
		}
		level_stalls <<= 1;
		n >>= 1;
	}
}

int main()
{
	int T;

	cin >> T;
	for (int i=0; i<T; i++)
	{
		ull n, k;
		cin >> n >> k;

		ull l, r;
		stall_spacings(n, k, l, r);
		cout << "Case #" << i+1 << ": ";
		cout << r << " " << l << endl;
	}
	return 0;
}