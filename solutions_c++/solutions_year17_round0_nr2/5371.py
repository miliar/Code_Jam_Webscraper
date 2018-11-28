#include <iostream>
#include <string>
#include <vector>
#include <array>
using namespace std;


int main()
{
	int cases = 0;
	cin >> cases;
	for (int T = 1; T <= cases; T++)
	{
		string N;
		cout << "Case #" << (T) << ": ";
		cin >> N;
		int lastDigit = N[N.length() - 1] - '0';
		for (int i = N.length()-2; i >= 0; i--)
		{
			int currentDigit = N[i] - '0';
			if (lastDigit >= currentDigit)
			{
				lastDigit = currentDigit;
				continue;
			}
			currentDigit--;
			N[i] = (currentDigit) + '0';
			for (unsigned int j = i+1; j < N.length(); j++)
			{
				N[j] = '9';
			}
			lastDigit = currentDigit;
		}

		if (N[0] == '0')
		{
			N = N.substr(1);
		}
		cout << N << endl;
	}
}