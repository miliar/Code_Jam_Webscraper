
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <cmath>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main(void)
{
	int t;
	long long n, k;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i)
	{
		cin >> n >> k;
		int ex = 0;
		int tmp = k;
		while (tmp > 1)
		{
			++ex;
			tmp /= 2;
		}
		long long remain = k - pow(2, ex);
		long long emptyStallCount = n - pow(2, ex) + 1;
		long long maxCount = emptyStallCount % (int)pow(2, ex);
		long long currentStallCount = emptyStallCount / (int)pow(2, ex);
		if (remain < maxCount)
		{
			currentStallCount += 1;
		}

		cout << "Case #" << i << ": " << (currentStallCount - 1) - (currentStallCount - 1) / 2 << " " << (currentStallCount - 1) / 2 << endl;
	}
	return 0;
}