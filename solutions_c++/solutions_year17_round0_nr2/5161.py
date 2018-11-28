#include <iostream>
#include <string>

using namespace std;


int main()
{
	int T;
	cin >> T;

	for (int t = 1; t<=T; ++t)
	{
		string S;
		cin >> S;

		cout << "Case #" << t << ": ";

		const int N = S.length();
		if (N < 2)
		{
			cout << S << endl;
			continue;
		}

		int i = 1;
		while (i < N && S[i-1] <= S[i])
			++i;

		if (i == N)
		{
			cout << S << endl;
			continue;
		}

		while (1)
		{
			--S[--i];
			if (i == 0 || S[i] >= S[i-1])
				break;
		}

		for (int j = i+1; j < N; ++j)
			S[j] = '9';

		if (S[i] == '0')
			cout << &(S.c_str()[i+1]) << endl;
		else
			cout << S << endl;
	}

	return 0;
}