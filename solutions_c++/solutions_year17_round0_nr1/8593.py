#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string findFlips(string S, int K);

int main()
{
	ifstream inFile("A-large.in");
	ofstream outFile("A-large.out");
	int T;
	int K;
	string S;

	inFile >> T;

	for (int i = 1; i <= T; i++)
	{
		inFile >> S;
		inFile >> K;

		outFile << "Case #" << i << ": " << findFlips(S, K) << endl;
	}

	return 0;
}

string findFlips(string S, int K)
{
	int flipsCount = 0;
	int index = 0;

	while (S.find_first_not_of("+") != string::npos)
	{
		for (index; index < S.length(); index++)
		{
			if (S.at(index) == '-')
				break;
		}

		if (index == S.length() && S.find_first_not_of("+") != string::npos)
			return "IMPOSSIBLE";
		else
		{
			if (index + K - 1 < S.length())
			{
				flipsCount++;
				for (int i = 0; i < K; i++)
				{
					if (S.at(index + i) == '+')
						S.at(index + i) = '-';
					else
						S.at(index + i) = '+';
				}
				index++;
			}
			else if (S.find_first_not_of("+") != string::npos)
				return "IMPOSSIBLE";
		}
	}

	return to_string(flipsCount);
}