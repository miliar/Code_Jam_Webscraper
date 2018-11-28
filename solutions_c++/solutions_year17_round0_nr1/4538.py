#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text





void main() {
	int t;

	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int testCase  = 1; testCase <= t; ++testCase) {
		string S;
		int K;

		cin >> S;
		cin >> K;

		int n = (int)S.size();

		int flips = 0;
		int i = 0;
		for (; i < n - K + 1; i++) {
			if (S[i] == '-') {
				flips++;
				for (int j = i; j < i + K; j++) {
					if (S[j] == '-')
						S[j] = '+';
					else
						S[j] = '-';
				}
			}
		}

		bool success = true;
		for (int j = i; j < n; j++) {
			if (S[j] == '-') {
				success = false;
				break;
			}
		}
		if (success) {
			cout << "Case #" << testCase << ": " << flips << endl;
		}
		else {
			cout << "Case #" << testCase << ": " << "IMPOSSIBLE" << endl;
		}




	}
}
