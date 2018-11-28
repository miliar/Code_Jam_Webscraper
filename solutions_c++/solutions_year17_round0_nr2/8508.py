#include <cctype>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> readNumber()
{
	vector<int> res;
	string input;
	cin >> input;
	for (int i = 0; i < input.length(); ++i) {
		if (!isdigit(input[i])) {
			cerr << "ERROR: expected digit" << endl;
			exit(EXIT_FAILURE);
		}
		res.push_back(input[i] - '0');
	}
	return res;
}

void printNumber(const vector<int> const &number)
{
	for (int i = 0; i < number.size(); ++i) {
		if (number[i] <= 0 || number[i] > 9)
			continue;
		cout << number[i];
	}
}

void makeTidy(vector<int> &number)
{
	bool hasChanged{ false };
	for (int i = 0; i < number.size() - 1; ++i) {
		if (number[i] > number[i + 1]) {
			number[i]--;
			for (int j = i + 1; j < number.size(); ++j) {
				number[j] = 9;
			}
			hasChanged = true;
			break;
		}
	}
	if (hasChanged) {
		makeTidy(number);
	}
}

int main()
{
	int cases;
	cin >> cases;
	if (cases < 0) {
		cerr << "ERROR: invalid number of test cases" << endl;
		exit(EXIT_FAILURE);
	}

	for (int i = 1; i <= cases; ++i) {
		vector<int> number = readNumber();
		makeTidy(number);
		cout << "Case #" << i << ": ";
		printNumber(number);
		cout << endl;
	}

	return 0;
}