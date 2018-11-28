#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <unordered_map>
#include <set>

using namespace std;

struct TestCase {
	int n, k;
	long double u;
	vector<long double> p;
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
		fs >> tc.n >> tc.k >> tc.u;
		for (int j = 0; j < tc.n; j++) {
			long double p;
			fs >> p;
			tc.p.push_back(p);
		}
		res.push_back(tc);
	}
	fs.close();
	return res;
}

template<typename Map>
bool contains(const Map& map, string word) {
	return map.find(word) != map.end();
}

std::string solve(TestCase& tc) {
	sort(tc.p.begin(), tc.p.end());
	vector<long double> p = tc.p;
	int n = (int)p.size();
	int fillTo = n;
	long double sumTo = 0;
	for (int i = 0; i < n; i++)
		sumTo += 1 - p[i];

	for (int i = 1; i < n; i++) {
		long double target = p[i];
		long double sum = 0;
		for (int j = 0; j < i; j++) {
			sum += target - p[j];
		}
		if (sum > tc.u) {
			fillTo = i;
			sumTo = sum;
			break;
		}
	}

	long double remaining = tc.u - sumTo;
	auto newP = p;
	long double maxP = fillTo >= n ? 1 : p[fillTo];
	for (int i = 0; i < fillTo; i++) {
		newP[i] = min((long double)1.0, maxP + (remaining / fillTo));
	}

	long double result = 1;
	for (int i = 0; i < (int)newP.size(); i++) {
		result *= newP[i];
	}
	result = result;
	return std::to_string(result);
}

int main(int argc, const char *argv[]) {
	std::ofstream fs("C-small-1-attempt0.out");
	int i = 1;
	auto cases = load("C-small-1-attempt0.in");
	for (auto it = cases.begin(); it != cases.end(); ++it) {
		fs << "Case #" << i << ": " << solve(*it) << endl;
		i++;
	}
	fs.close();

	return 0;
}
