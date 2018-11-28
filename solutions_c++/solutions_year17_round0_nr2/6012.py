#include <iostream>
#include <vector>
using namespace std;

void get_last_num(string &input) {
	int len = input.length();

	if (len < 2)
		return;

	char prev = input[0];
	int i = 1;
	for (; i < len; ++i) {
		if ((prev - '0') > (input[i] - '0'))
			break;
		prev = input[i];
	}

	if (i == len)
		return;

	for (int j = i; j < len; ++j)
		input[j] = '9';

	input[--i] -= 1;

	while (i > 0 && input[i] == '0' || input[i - 1] > input[i]) {
		input[i] = '9';
		input[--i] -= 1;
	}

	if (i == 0 && input[i] == '0')
		input.erase(0, 1);
}

int main()
{
	int T;
	string input;

	cin >> T;

	for (int i = 0; i < T; ++i) {
		cin >> input;
		get_last_num(input);

		cout << "Case #" << i + 1 << ": " << input << endl;
	}
}
