#include <iostream>
using namespace std;

int main() {
    int ncase = 0;
    cin >> ncase;
    for (int round = 1; round <= ncase; ++round) {
		string input;
		int k;
		cin >> input;
		cin >> k;
		int count = 0;
		for (int i = 0; i < (int)input.length() - k + 1; ++i) {
			if (input[i] == '-') {
				count++;
				for(int j = 0; j < k; ++j) {
					if (input[i + j] == '-') input[i + j] = '+';
					else input[i + j] = '-';
				}
			}
		}
        cout << "Case #" << round << ": ";
		if (input.substr(input.length() - k, k).find("-") != string::npos)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << count << endl;
	}
    return 0;
}
