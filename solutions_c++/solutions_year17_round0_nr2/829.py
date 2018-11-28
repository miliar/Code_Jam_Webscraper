#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

long long tiny(long long num)
{
	vector<int> digits;
	while (num > 0)
	{
		digits.push_back(num % 10);
		num /= 10;
	}
	for (int i = digits.size() - 1; i > 0; --i)
	{
		bool found = false;
		for (int j = digits.size() - 1; j > 0; --j)
		{
			if (digits[j] > digits[j - 1])
			{
				found = true;
				digits[j]--;
				for (int k = j - 1; k >= 0; --k)
				{
					digits[k] = 9;
				}
				break;
			}
		}
		if (!found) break;
	}
	long long res = 0, factor = 1;
	for (int i = 0; i < digits.size(); ++i)
	{
		res += digits[i] * factor;
		factor *= 10;
	}

	return res;
}

int main(int argc, char* argv[])
{
	int t;
	cin >> t;
	
	for (int i = 1; i <= t; ++i)
	{
		long long input;
		cin >> input;
		long long res = tiny(input);

		cout << "Case #" << i << ": " << res <<'\n';
	}
	return 0;
}