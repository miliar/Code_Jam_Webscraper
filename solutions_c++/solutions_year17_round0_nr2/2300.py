#include <iostream>
#include <string>

using namespace std;

string algorithm(string input_s, int current_pos) {
	if (current_pos<0) { return algorithm(input_s, 0); }
	if (current_pos == input_s.length() - 1) {
		return input_s;
	}
	unsigned int p0, p1;
	p0 = stoi(input_s.substr(current_pos, 1), NULL, 10);
	p1 = stoi(input_s.substr(current_pos + 1, 1), NULL, 10);
	if (p0>p1) {
		input_s.replace(current_pos + 1, input_s.length() - (current_pos + 1), input_s.length() - (current_pos + 1), '9');
		int i;
		for (i = current_pos;i>-1;i++) {
			unsigned int current_at = stoi(input_s.substr(i, 1), NULL, 10);
			if (current_at>0) {
				current_at--;
				input_s.replace(i, 1, to_string(current_at));
				break;
			}
			else {
				input_s.replace(i, 1, "9");
			}
		}
		return algorithm(input_s, i - 1);
	}
	else { return algorithm(input_s, current_pos + 1); }
}

int main()
{
	unsigned int tc_count;
	cin >> tc_count;
	for (unsigned int tc = 0;tc<tc_count;tc++) {
		unsigned long long int input;
		cin >> input;
		string input_s;
		input_s = to_string(input);
		input_s = algorithm(input_s, 0);
		unsigned int lim = input_s.length();
		for (unsigned int i = 0;i<lim - 1;i++) {
			if (input_s.at(0) == '0') {
				input_s.erase(input_s.begin());
			}
			else { break; }
		}
		cout << "Case #" << tc + 1 << ": " << input_s << '\n';
	}
	return 0;
}
