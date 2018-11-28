#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <unordered_map>
#include <unordered_set>

using namespace std;

struct TestCase {
	std::string pancakes;
	int k;
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
		fs >> tc.pancakes;
		fs >> tc.k;
		res.push_back(tc);
	}
	fs.close();
	return res;
}

std::string flip(const std::string& src, int from, int to) {
	std::string res = src;
	for (int i = from; i < to; i++) {
		if (res[i] == '-')
			res[i] = '+';
		else
			res[i] = '-';
	}
	return res;
}

std::string solve(TestCase& tc) {
	std::unordered_set<std::string> visited;
	list<pair<string, int>> queue;
	queue.push_back(make_pair(tc.pancakes, 0));
	visited.insert(tc.pancakes);
	while (!queue.empty()) {
		auto entry = queue.front();
		if (entry.first.find("-") == std::string::npos)
			return std::to_string(entry.second);
		queue.pop_front();
		for (int i = 0; i < (int)entry.first.length() - tc.k + 1; i++) {
			std::string newVal = flip(entry.first, i, i + tc.k);
			if (visited.find(newVal) == visited.end()) {
				queue.push_back(make_pair(newVal, entry.second + 1));
				visited.insert(newVal);
			}
		}
	}
	return "IMPOSSIBLE";
}

std::string solve2(TestCase& tc) {
	std::unordered_set<std::string> visited;
	std::string current = tc.pancakes;
	int res = 0;
	for (int i = 0; i < current.length() - tc.k + 1; i++) {
		if (current[i] == '-') {
			res++;
			current = flip(current, i, i + tc.k);
		}
	}
	if (current.find('-') != std::string::npos)
		return "IMPOSSIBLE";
	return std::to_string(res);
}

int main(int argc, const char *argv[]) {
	std::ofstream fs("A-large.out");
	int i = 1;
	for (auto tc : load("A-large.in")) {
		fs << "Case #" << i << ": " << solve2(tc) << std::endl;
		i++;
	}
	fs.close();
	return 0;
}
