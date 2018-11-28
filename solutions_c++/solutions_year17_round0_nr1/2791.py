#include <iostream>
#include <string>

using namespace std;

void main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		string S;
		cin >> S;
		int K;
		cin >> K;

		int flips = 0;

		for (size_t i = 0; i <= S.size() - K; ++i)
		{
			if (S[i] == '-')
			{
				for (int k = 0; k < K; ++k)
				{
					auto& c = S[i + k];
					c = c == '-' ? '+' : '-';
				}
				++flips;
			}
		}
		cout << "Case #" << t + 1 << ": ";
		if (S.find('-', S.size() - K + 1) == string::npos)
		{
			cout << flips;
		}
		else
		{
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
}
