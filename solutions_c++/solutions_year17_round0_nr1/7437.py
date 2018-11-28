// PanCake.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>

using namespace std;
int numTestCases, z;
int K;
string S;


int main()
{
	cin >> numTestCases;

	for (int t = 1; t <= numTestCases; ++t) {
		
		cin >> S >> K;

		cout << "Case #" << t << ": ";

		int count = 0, j;
		int size = S.size();

		if (size < K)
		{
			cout << "IMPOSSIBLE" << endl;
			break;
		}	

		for (int i = 0; i < size; ++i)
		{
			if (i + K < size)
			{
				if (S[i] == '+') continue;
				for (j = 0; j < K; ++j)
				{
					if (S[i + j] == '+') S[i + j] = '-';
					else if (S[i + j] == '-') S[i + j] = '+';
				}
				++count;
			}
			else if (i + K == size)
			{
				int numPlus = 0;
				int numMinus = 0;
				for (j = 0; j < K; ++j)
				{
					if (S[i + j] == '+') ++numPlus;
					else if (S[i + j] == '-') ++numMinus;

					if (numPlus > 0 && numMinus > 0)
						break;
				}

				if (numMinus == 0)
					cout << count << endl;
				else if (numPlus == 0)
					cout << ++count << endl;
				else
					cout << "IMPOSSIBLE" << endl;
			}
		}
	}
	return 0;
}

