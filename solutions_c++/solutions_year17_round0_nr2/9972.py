#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>

using namespace std;

class TidyNumbers 
{
public:
	long long getTidyNumber(long long N) 
	{
		long long i = N;
		for (long long i = N; i > 0; --i)
		{
			if (isTidy(i))
			{
				return i;
			}
		}
		return 0;
	}
	bool isTidy(long long N) 
	{
		long long m = 9; // max so far
		while(N > 0)
		{
			long long n = N % 10;
			if (n > m)
			{
				return false;
			}
			m = n;
			N /= 10;
		}
		return true;
	}
};

int main()
{
	int T = 0;
	cin >> T;

	for (int t = 0; t < T; ++t)
	{
		long long N = 0;
		cin >> N;

		TidyNumbers tn;
		cout << "Case #" << t + 1 << ": " << tn.getTidyNumber(N) << endl;
	}

	return 0;
}
