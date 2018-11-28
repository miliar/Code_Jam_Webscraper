#include <iostream>
#include <string>
using namespace std;

string do_process(string input) {
	int start = -1;
	if (input.length() == 1) return input;
	for (int i = 0; i < input.length() - 1; ++i) {
		if(input[i] > input[i+1]) {
			input[i] = input[i] - 1;
			start = i + 1;
			break;
		}
	}
	if (start > 0) {
		for (int i = start - 2; i >= 0; --i) {
			if(input[i] > input[i+1]) {
				input[i] = input[i] - 1;
				start = i + 1;
			}
		}

		for (int i = start; i <= input.length(); ++i) {
			input[i] = '9';
		}
	}

	size_t found = input.find_first_not_of("0");
	if (found == string::npos) return "0";
	return input.substr(found);
}

int main() {
    int ncase = 0;
    cin >> ncase;
    for (int round = 1; round <= ncase; ++round) {
        string input;
        cin >> input;

	    string output = do_process(input);
        cout << "Case #" << round << ": ";
        cout << output << endl;
    }
    return 0;
}
