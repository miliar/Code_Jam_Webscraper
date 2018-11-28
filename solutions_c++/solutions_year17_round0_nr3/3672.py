#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

void solve(int testCase, ifstream &input, ofstream &output) {
	int64_t n, k;
	input >> n >> k;

	vector<int64_t> options;

	options.push_back(n);

	int64_t ls = 0;
	int64_t rs = 0;

	for (int64_t i = 0; i < k; i++) {
		cout << "Looking at person no. " << i + 1 << endl;

		int64_t optionIndex = 0;

		for (int64_t j = 0; j < options.size(); j++) {
			if (options[optionIndex] < options[j]) {
				optionIndex = j;
			}
		}

		//cout << "Biggest option: " << options[optionIndex] << endl;

		if (options[optionIndex] % 2 == 0) {
			ls = options[optionIndex] / 2 - 1;
			rs = options[optionIndex] / 2;

			if (options[optionIndex] / 2 - 1 > 0) options.push_back(options[optionIndex] / 2 - 1);
			options[optionIndex] /= 2;
		} else {
			ls = options[optionIndex] / 2;
			rs = options[optionIndex] / 2;

			if (options[optionIndex] / 2 > 0) options.push_back(options[optionIndex] / 2);
			options[optionIndex] /= 2;
		}

		cout << "LS: " << ls << endl;
		cout << "RS: " << rs << endl;

		//cout << "Vector state: ";

		/*for (int64_t j = 0; j < options.size(); j++) {
			cout << options[j] << " ";
		}*/

		//cout << endl;
	}
 
	output << "Case #" << testCase << ": ";

	if (ls > rs) {
		output << ls << " " << rs << endl;
	} else {
		output << rs << " " << ls << endl;
	}
}

void solve2(int testCase, ifstream &input, ofstream &output) {
	int64_t n, k;
	input >> n >> k;

	int64_t ls = 0;
	int64_t rs = 0;

	map<int64_t, int64_t> options;
	options.insert(make_pair(n, 1));

	while (k > 0) {
		//cout << "K: " << k << endl;

		int64_t max = 0;

		for (const auto &pair : options) {
			//cout << pair.first << ": " << pair.second << " ";

			if (pair.first > max) {
				max = pair.first;
			}
		}

		//cout << endl;

		int64_t amount = options.at(max);
		k -= amount;

		//cout << "Decreased by " << amount << endl;

		options.erase(max);

		//cout << "Removed " << max << endl;

		int64_t firstOption = 0;
		int64_t secondOption = 0;

		if (max % 2 == 0) {
			firstOption = max / 2 - 1;
		} else {
			firstOption = max / 2;
		}

		secondOption = max / 2;

		for (int i = 0; i < amount; i++) {
			auto find = options.find(firstOption);
			if (find == options.end()) {
				options.insert(make_pair(firstOption, 1));
			} else {
				find->second++;
			}

			find = options.find(secondOption);
			if (find == options.end()) {
				options.insert(make_pair(secondOption, 1));
			} else {
				find->second++;
			}
		}

		ls = firstOption;
		rs = secondOption;
	}
 
	output << "Case #" << testCase << ": ";

	if (ls > rs) {
		output << ls << " " << rs << endl;
	} else {
		output << rs << " " << ls << endl;
	}
}

int main(int argc, char *argv[]) {
	if (argc > 0) {
		ofstream outputFile(argv[2]);
		ifstream inputFile(argv[1]);

		int t;
		inputFile >> t;

		for (int i = 0; i < t; i++) {
			cout << "Solving case " << i + 1 << endl;

			solve2(i + 1, inputFile, outputFile);
		}
	}

	return 0;
}