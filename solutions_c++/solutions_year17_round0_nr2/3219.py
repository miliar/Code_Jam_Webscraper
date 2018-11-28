#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for (int N = 1; N <= T; N++)
	{
		__int64 n;
		cin >> n;
		vector<int> digits;
		while (n != 0)
		{
			digits.push_back(n % 10);
			n /= 10;
		}
		vector<int> out(digits.size());
		bool carry;
		do
		{
			carry = false;
			for (int i = 0; i<digits.size() - 1; i++)
				if (digits[i]<digits[i + 1])
					digits[i] = 10, digits[i+1]--, carry = true;
		} while (carry);
		int digit = 9;
		for (int i = 0; i < digits.size();i++)
		{
			digit = min(digit, digits[i]);
			out[i] = digit;
		}
		cout << "Case #" << N << ": ";
		n = 0;
		for (int i = out.size() - 1; i >= 0; i--)
			n = n * 10 + out[i];
		cout << n << endl;
	}
	return 0;
}