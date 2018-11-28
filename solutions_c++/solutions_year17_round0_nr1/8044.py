#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int k;
		string s;
		cin >> s >> k;
		vector<int> flips(s.length(), 0);
		int flipsCount = 0;
		int stepsCount = 0;
		for (int i = 0; i < s.length() && stepsCount >= 0; ++i) {
			flipsCount += flips[i];
			if (!(s[i] == '+' && flipsCount % 2 == 0 || s[i] == '-' && flipsCount % 2)) {
                if (i + k <= s.length()) {
                    ++flipsCount;
                    ++stepsCount;
                    if (i + k < s.length()) {
                        --flips[i + k];
                    }
                } else {
                    stepsCount = -1;
                    break;
                }
			}
		}

        cout << "Case #" << t << ": ";
        if (stepsCount < 0) {
            cout << "IMPOSSIBLE";
        } else {
            cout << stepsCount;
        }
        cout << endl;
	}
	return 0;
}