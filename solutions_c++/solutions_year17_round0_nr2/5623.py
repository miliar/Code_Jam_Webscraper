#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <unordered_map>

using namespace std;

struct TestCase {
	string number;
};

std::vector<TestCase> load(const std::string& s) {
	std::ifstream fs(s);
	if (!fs.is_open())
		std::cout << "Not found" << std::endl;

	int n;
	std::vector<TestCase> res;
	fs >> n;
	for (int i = 0; i < n; i++) {
		TestCase tc;
		fs >> tc.number;
		res.push_back(tc);
	}
	fs.close();
	return res;
}

int invalidPos(const std::string& number) {
	for (int i = 1; i < number.length(); i++) {
		if (number[i - 1] > number[i])
			return i;
	}
	return number.length();
}

std::string zeros(const std::string& number, int from) {
	std::string res = number;
	for (int i = from; i < res.length(); i++)
		res[i] = '0';
	return res;
}

std::string solve(TestCase& tc) {
	std::string current = tc.number;
	int pos = invalidPos(current);
	while (pos < current.length()) {
		unsigned long long number = std::stoull(zeros(current, pos), nullptr, 10);
		if (number == 0) {
			std::cout << "Warning, got 0" << std::endl;
			return "0";
		}
		number--;
		current = std::to_string(number);
		pos = invalidPos(current);
	}
	return current;
}

int main(int argc, const char *argv[]) {
	std::ofstream fs("B-large.out");
	int i = 1;
	for (auto tc : load("B-large.in")) {
		fs << "Case #" << i << ": " << solve(tc) << std::endl;
		i++;
	}
	fs.close();
	return 0;
}

