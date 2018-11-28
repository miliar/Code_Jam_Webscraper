#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		string S;
		size_t K;
		cin >> S >> K;
		vector<bool> endOfFlipper(S.size(), false);
		int ret = 0;
		bool notFlipped = true;
		for (size_t i = 0; i < S.size(); ++i) {
			bool happy = (S[i] == '+');
			if (happy != notFlipped) {
				// Need to flip
				if (i + K > S.size()) {
					ret = -1;
					break;
				}
				// Flip here
				++ret;
				endOfFlipper[i + K - 1] = true;
				notFlipped = !notFlipped;
			}
			if (endOfFlipper[i])
				notFlipped = !notFlipped;
		}
		cout << "Case #" << (t+1) << ": ";
		if (ret == -1) {
			cout << "IMPOSSIBLE";
		} else {
			cout << ret;
		}
		cout << endl;
	}
	return 0;
}
