#include <iostream>
#include <string>

using namespace std;

void process(string s) {
	// all good while s[i] >= s[i-1]; then, decrease s[0:i] and 9-pad
	for (size_t i = 1; i < s.size(); ++i) {
		if (s[i] < s[i-1]) {
			for (size_t j=i+1;j<s.size();++j) {
                                s[j] = '9';
                        }
			do {
				s[i]='9';
				if (s[i-1]=='0') {
					s[i-1]='9';
				} else {
					--s[i-1];
				}
				--i;
			} while (s[i] < s[i-1]);
			break;
		}
	}
	cout << s.substr(s.find_first_not_of("0")) << endl;
}

int main(int argc, char** argv) {
	size_t inputCount;
	cin >> inputCount;
	for (size_t inputNumber = 1; inputNumber <= inputCount; ++inputNumber) {
		string s;
		cin >> s;
		cout << "Case #" << inputNumber << ": ";
		process(s);
	}
	return 0;
}
