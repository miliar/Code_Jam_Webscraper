#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <cstdint>
#include <set>

using namespace std;

struct TestCase {
	unsigned long long n, k;
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
		fs >> tc.n >> tc.k;
		res.push_back(tc);
	}
	fs.close();
	return res;
}

pair<uint64_t, uint64_t> sumPowerOf2(uint64_t nr) {
	uint64_t res = 0;
	uint64_t a = 1;
	while (res + a < nr) {
		res += a;
		a *= 2;
	}
	return make_pair(res, a);
}

std::string solve(TestCase& tc) {
	auto sumAndPower = sumPowerOf2(tc.k);
	uint64_t largestGap = tc.n / (sumAndPower.first + 1);
	uint64_t k_rest = tc.k - sumAndPower.first;
	uint64_t gaps = sumAndPower.second;
	uint64_t normalGap = largestGap - 1;
	uint64_t largestGapSmallHalf = largestGap % 2 == 0 ? largestGap / 2 - 1 : largestGap / 2;
	if (k_rest == 0)
		return std::to_string(largestGap) + " " + std::to_string(normalGap);
	if (k_rest == 1)
		return std::to_string(largestGap / 2) + " " + std::to_string(largestGapSmallHalf);

	uint64_t normalGapSmallHalf = normalGap % 2 == 0 && normalGap != 0 ? normalGap / 2 - 1 : normalGap / 2;
	return std::to_string(normalGap / 2) + " " + std::to_string(normalGapSmallHalf);
	// o.o.o.o.o.o.o.o..o
	// o.o.o.o.o...o.o..o
}

std::string solveBrute(TestCase& tc) {
	multiset<uint64_t, greater<uint64_t>> intervals;
	intervals.insert(tc.n);
	int k = (int)tc.k;
	uint64_t currentMin = tc.n;
	uint64_t currentMax = 0;
	while (k > 0) {
		auto largest = *intervals.begin();
		auto small = largest % 2 == 0 ? largest / 2 - 1 : largest / 2;
		auto big = largest / 2;
		intervals.erase(intervals.begin());
		intervals.insert(small);
		intervals.insert(big);
		currentMin = small;
		currentMax = big;
		k--;
	}
	return std::to_string(currentMax) + " " + std::to_string(currentMin);
}

int main(int argc, const char *argv[]) {
	std::ofstream fs("C-small-1-attempt2.out");
	int i = 1;
	auto cases = load("C-small-1-attempt2.in");
	for (auto it = cases.begin(); it != cases.end(); ++it) {
		fs << "Case #" << i << ": " << solveBrute(*it) << std::endl;
		i++;
	}
	fs.close();

	return 0;
}
