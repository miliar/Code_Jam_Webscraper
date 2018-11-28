#include <iostream>
#include <string>
using namespace std;



int main()
{
	int cases = 0;
	cin >> cases;
	for (int T = 1; T <= cases; T++)
	{
		cout << "Case #" << (T) << ": " ;
		unsigned int flips = 0;
		string S;
		S = "";
		unsigned int K;
		cin >> S;
		cin >> K;
		string Sk;
		bool impossiable = false;
		for (unsigned int i = 0; i < S.length() - K; i++)
		{
			if (S[i] == '+') continue;
			flips++;
			for (unsigned int j = 0; j < K; j++)
			{
				if (S[i+j] == '+')
					S[i+j] = '-';
				else
					S[i+j] = '+';
			}
		}
		bool first = true;
		char c = '2';
		for (unsigned int i = S.length() - K; i < S.length(); i++)
		{
			if (first) {
				c = S[i];
				first = false;
			};
			if (S[i] != c)
			{
				impossiable = true;
				break;
			}
		}
		if (impossiable)
			cout << "IMPOSSIBLE" << endl;
		else
		{
			if (c == '-') flips++;
			cout << flips << endl;
		}
	}
}