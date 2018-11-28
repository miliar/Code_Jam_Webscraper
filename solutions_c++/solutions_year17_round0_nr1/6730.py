#include <iostream>
#include <string>
using namespace std;

int T, K, counter;
string cake;

void flips()
{
	int limit = cake.size() - K;
	for (int i = 0; i <= limit; i++)
		if (cake[i] == '-')
		{
			counter++;
			for (int j = 0; j < K; j++)
				if (cake[i + j] == '-')
					cake[i + j] = '+';
				else
					cake[i + j] = '-';
		}
}

bool checkHappy()
{
	for (int i = 0; i < (signed)cake.size(); i++)
		if (cake[i] == '-')
			return false;
	
	return true;
}

int main()
{
	cin >> T;
	for (int testCase = 1; testCase <= T; testCase++)
	{
		cake.clear();
		counter = 0;

		cin >> cake;
		cin >> K;

		flips();

		cout << "Case #" << testCase << ": ";
		if (checkHappy() == true)
			cout << counter;
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}

	return 0;
}