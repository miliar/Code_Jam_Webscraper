#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;  

bool check(string S)
{
	for (int i = 0; i < S.length(); i++)
		if (S[i] == '-')
			return false;
	return true;
}

void main()  
{  
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		string S;
		int K;
		cin >> S;
		cin >> K;

		int length = S.length();
		int counter = 0;

		for (int j = 0; j <= length - K; j++)
		{
			if (S[j] == '+')
				continue;

			counter++;

			for (int k = 0; k < K; k++)
			{
				if (S[j + k] == '+')
					S[j + k] = '-';
				else
					S[j + k] = '+';
			}
		}

		if (check(S))
			cout << "Case #" << i+1 << ": " << counter << endl;
		else 
			cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
	}
}  