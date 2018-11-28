#include <iostream>
#include <string>
using namespace std;
string getTidy(string);

int ctoi(char c) {
	return c - '0';
}
string makeTidy(string input, int index){
	input[index - 1] = '0' + (ctoi(input[index - 1]) - 1);
	for (int i = index; i != input.size(); ++i) {
		input[i] = '0' + 9;
	}
	int nonzero = 0;
	while(input[nonzero] == '0') {
		nonzero++;
	}
	return getTidy(string(input.begin() + nonzero, input.end()));
}
string getTidy(string input) {
	string result = input;
	int prev = ctoi(input[0]);
	for (int i = 1; i != input.size(); ++i) {
		int curr = ctoi(input[i]);
		if (curr < prev) {
			return makeTidy(input, i);
		}
		prev = curr;
	}
	return input;
}
int main() {
	int n = 0;
	string input, output;
	cin >> n;
	for (int i = 0; i != n; ++i) {
		cin >> input;
		output = getTidy(input);
		cout << "Case #" << i + 1 << ": " << output <<  endl; 
	}
	return 0;
}