#include <iostream>
#include <cmath>

using namespace std;

long long unsigned int pow10(int n)
{
	long long unsigned int result;
	for(result = 1; n > 0; n--)
	{
		result *= 10;
	}
	return result;
}

int main()
{
	int t;
	cin >> t;

	for(int i = 0; i < t; i++)
	{
		long long unsigned int n, tidy_num, multiplier = 1;
		cin >> n;

		//cout << "Input = " << n << endl;

		tidy_num = n % 10;
		int last_digit = n % 10;
		n /= 10;
		for(int ndigit = 1; n > 0; n /= 10, ndigit++)
		{
			//cout << "tidy_num = " << tidy_num << endl;
			//cout << "n = " << n << endl;

			int current_digit = n % 10;
			if(last_digit < current_digit)
			{
				tidy_num = pow10(ndigit) - 1;
				n -= 1;
			}
			tidy_num = tidy_num + pow10(ndigit) * (n % 10);
			last_digit = n % 10;

			//cout << "last_digit = " << last_digit << endl;
		}

		cout << "Case #" << (i + 1) << ": " << tidy_num << endl; 
	}
	return 0;
}
