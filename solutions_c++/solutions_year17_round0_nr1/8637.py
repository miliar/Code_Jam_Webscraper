#include<iostream>
#include<string>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A_large.out", "w", stdout);

	int T;
	cin >> T;

	for (int t=1; t<=T; ++t) {

		string S;
		cin >> S;

		int K;
		cin >> K;

		int ans = 0;

		for (int i=0; i<=S.length()-K; ++i) {
			if (S[i] == '-') {
				++ans;
				for (int j=i; j<i+K; ++j) {
					S[j] = (S[j] == '+' ? '-' : '+');
				}
			}
		}

		bool isPossible = true;
		for (int i=0; i<S.length(); ++i) {
			if (S[i] == '-') {
				isPossible = false;
			}
		}

		cout << "Case #" << t << ": " << (isPossible ? to_string(ans) : "IMPOSSIBLE") << endl;
	}

	return 0;
}