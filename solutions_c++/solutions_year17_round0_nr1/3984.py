#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int c = 0; c < T; ++c) {
		string S;
		cin >> S;
		int K;
		cin >> K;

		int r = 0, steps = 0;
		while (S[++r] == S[0])
			;
		if (S[0] == '-') {
			steps = r/K;
		}
		S.erase(0, K*(r/K));
		int pos = S.find('-');
		while(S.size() >= K && pos <= S.size() - K && pos != string::npos) {
			for (int i = pos; i < pos + K; ++i) {
				if (S[i] == '+')
					S[i] = '-';
				else
					S[i] = '+';
			}
			++steps;
			pos = S.find('-', pos+1);
			//cout << S << endl << pos << endl;
		}
		cout << "Case #" << (c+1) << ": ";
		if (pos == string::npos)
			cout << steps << "\n";
		else
			cout << "IMPOSSIBLE\n";
	}

	return 0;
}
