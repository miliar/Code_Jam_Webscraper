#include <iostream>
#include <vector>
#include <string>

using namespace std;

string tidyUp(string n) {
	bool started = false;
	for (unsigned int i = 0; i < n.length() - 1; i++) {
		if (n[i] > n[i + 1]) {
			if (!started) {
				n[i] = n[i] - 1;
				n[i + 1] = '9';
				started = true;
			} else {
				n[i + 1] = n[i];
			}
		}
	}
	while (n[0] == '0' && n.length() > 1) {
		n.erase(0, 1);
	}
	if (started) {
		return tidyUp(n);
	}
	return n;
}

int main() {
	unsigned int T = 0;
	cin >> T;
	for (unsigned int i = 0; i < T; i++) {
		string input = "";
		cin >> input;

		cout << "Case #" << (i + 1) << ": " << tidyUp(input) << endl;
	}
}