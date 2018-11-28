#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <random>

using namespace std;

vector<int> splitToDigits(string input) {
	vector<int> digits;
	for (char c : input)
		digits.push_back(c - '0');
	return digits;
}

bool isTidy(vector<int> number) {
	int maxVal = 0;
	for (int digit:number) {
		if (digit < maxVal)
			return false;
		maxVal = digit;
	}
	return true;
}

vector<int> solveCase(string input) {
	vector<int> digits = splitToDigits(input);
	if (isTidy(digits))
		return digits;
	
	int i = 0;
	for (;i<digits.size()-1;i++) {
		if (digits[i] > digits[i+1]) {
			//edge case: move pointer to More Significant Digits since we can't desrease 0
			while (digits[i] == 0)
				--i;
			while (i > 0 && digits[i - 1] == digits[i])
				--i;

			digits[i]--;
			break;
		}
	}
	i++;
	for (; i < digits.size(); i++)
		digits[i] = 9;

	return digits;


}

string vecToStr(const vector<int> digits) {
	stringstream ss;
	for (const int d : digits)
		ss << d;
	return ss.str();
}

int vecToInt(const vector<int> digits){
	int val = 0;
	int mult = 1;
	for (auto i =digits.rbegin(); i!=digits.rend();++i) {
		val += *i * mult;
		mult *= 10;
	}
	return val;
}

vector<int> naiveSolution(string valueString) {
	vector<int> digits;
	do {
		digits = splitToDigits(valueString);
		int value = stoi(valueString);
		value--;
		valueString = to_string(value);
	} while (!isTidy(digits));

	return digits;
}

void main() {
	int cases;
	cin >> cases;
	for (int i=0;i<cases;i++) {
		string value;
		cin >> value;
		auto solution = solveCase(value);
		cout << "Case #" << i + 1 << ": " << stoll(vecToStr(solution)) << endl;
	}
	//random_device rd;
	//mt19937 eng(rd());
	//uniform_int_distribution<int> dist(1, 1000);
	//
	//for (int i=0;i<10000;i++) {
	//	int val = dist(eng);
	//	string valStr = to_string(val);
	//	if (vecToInt(solveCase(valStr)) != vecToInt(naiveSolution(valStr)))
	//		cout << "For " << val << " expected " << vecToInt(naiveSolution(valStr)) << " but got" << vecToInt(solveCase(valStr)) << endl;
	//}
}