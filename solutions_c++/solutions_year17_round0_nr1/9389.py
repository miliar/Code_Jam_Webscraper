#include <string>
#include <iostream>
using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		string S;
		int K;
		cin >> S >> K;

		int ret = 0;
		for (int j = 0; j <= S.length() - K; ++j)
		{
			if (S[j] == '-')
			{
				++ret;
				for (int k = 0; k < K; ++k)
					if (S[j + k] == '+')
						S[j + k] = '-';
					else
						S[j + k] = '+';
			}
		}

		bool fGood = true;
		for (int j = 0; j < S.length(); ++j)
			if (S[j] == '-')
			{
				fGood = false;
				break;
			}
		
		if (fGood)
			cout << "Case #" << i + 1 << ": " << ret << endl;
		else
			cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
	}
}