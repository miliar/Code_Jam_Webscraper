#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	size_t T; cin >> T;

	for (size_t i = 0; i < T; ++i)
	{
		uint64_t N; cin >> N;

		uint64_t n = N;

		for (uint64_t j = 10; j <= n; j *= 10)
		{
			bool c = false;
			for (uint64_t j2 = j; j2 <= n * 10; j2 *= 10)
			{
				uint64_t m1 = (n % j2) / (j2 / 10);
				uint64_t s1 = (n % (j2 * 10)) / j2;
				if (m1 < s1) c = true;
			}

			if (c)
			{
				n -= (((n % j) / (j / 10)) + 1) * j / 10;
			}
		}

		cout << "Case #" << i + 1 << ": " << n << endl;

	}

	return 0;
}