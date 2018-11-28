#include <iostream>
#include <string>

using namespace std;

int solve(string S, const int K)
{
	int i, j, flips = 0;
	const int N =  S.length();
	for (i = K; i <= N; ++i)
	{
		if (S[i-K] == '-') {
			++flips;
			for (j = i-K; j < i; ++j)
				S[j] = (S[j]=='-'?'+':'-');
		}
	}

	for (i -= K; i < N; ++i)
		if (S[i]=='-')
			return -1;

	return flips;
}

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t<=T; ++t)
	{
		string S;
		int K;
		cin >> S;
		cin >> K;

		int sol = solve(S,K);
		cout << "Case #"<<t<<": ";
		if (sol >= 0)
			cout << sol << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}