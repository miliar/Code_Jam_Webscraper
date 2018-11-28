#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <unordered_map>
#include <map>

using namespace std;

struct Horse {
	long long k;
	long long s;
};

struct TestCase {
	long long d;
	vector<Horse> horses;
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
		fs >> tc.d;
		int h;
		fs >> h;
		for (int j = 0; j < h; j++) {
			Horse horse;
			fs >> horse.k;
			fs >> horse.s;
			tc.horses.push_back(horse);
		}
		res.push_back(tc);
	}
	fs.close();
	return res;
}

std::string solve(TestCase& tc) {
	long double minV = std::numeric_limits<long double>::infinity();
	for (Horse& horse : tc.horses) {
		long double time = (tc.d - horse.k) / (long double)horse.s;
		long double v = tc.d / time;
		minV = std::min(minV, v);
	}
	return std::to_string(minV);
}

int main(int argc, const char *argv[]) {
	std::ofstream fs("A-large.out");
	int i = 1;
	for (auto tc : load("A-large.in")) {
		fs << "Case #" << i << ": " << solve(tc) << std::endl;
		std::cout << i << endl;
		i++;
	}
	fs.close();
	return 0;
}
