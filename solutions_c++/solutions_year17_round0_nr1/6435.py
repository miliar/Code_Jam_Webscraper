#include <iostream>
#include <vector>

using namespace std;

int main() {

	int P;
	cin >> P;
	for (int p = 1; p <= P; p++) {
		cout << "Case #" << p << ": ";
		string s;
		cin >> s;
		int w;
		cin >> w;
		vector<int> ss;
		for (int i = 0; i < s.size() ; i++) {
			if (s[i] == '+') {
				ss.push_back(1);
			} else {
				ss.push_back(-1);
			}
		}
		int flips = 0;
		for (int i = 0; i <= ss.size() - w; i++) {
			if (ss[i] == -1) {
				for (int j = i; j < i + w; j++) {
					ss[j] *= -1;
				}
				flips++;
			}
		}
		for (int i : ss) {
			if (i == -1) {
				cout << "IMPOSSIBLE" << endl;
				goto nextP;
			}
		}
		cout << flips << endl;
		nextP:
		continue;
	}

}
