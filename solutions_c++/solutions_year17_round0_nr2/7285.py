#include <iostream>
#include <string>

using namespace std;

void changeLine (string & line) {
	int len = line.size();
	for (int i=len-1; i>0; i--) {
		if (line[i] < line[i-1]) {
			char nChar = line[i-1] - 1;
			line = line.substr(0, i-1) + nChar + string(len - i, '9');
			// cout << line;
		}
	}

	if (line[0] == '0')
		line = line.substr(1);
}

int main () {
	int T;
	string line;
	cin >> T;

	// T = 1;

	for (int rowNum =1; rowNum <= T; rowNum++) {
		cin >> line;

		changeLine(line);

		cout << "Case #" << rowNum << ": " << line << endl;
	}
}