#include <iostream>
#include <set>
#include <queue>
#include <string>
#include <fstream>

bool all_happy(const std::string& s) {
	for (auto it = s.begin(); it != s.end(); ++it) {
		if (*it != '+') return false;
	}
	return true;
}

std::string flip(const std::string& s, int k, int start_index) {
	std::string t = s;
	for (int i = start_index; i < start_index + k; i++) {
		t[i] = t[i] == '+' ? '-' : '+';
	}
	return t;
}

int search(const std::string& init, const int& k) {
	// std::unordered_map<std::string, bool> seen;
	std::set<std::string> seen;
	std::queue<std::pair<std::string, int>> q;

	q.push(std::make_pair(init, 0));
	while (!q.empty()) {
		std::pair<std::string, int> p = q.front();
		q.pop();

		if (all_happy(p.first)) {
			return p.second;
		}

		seen.insert(p.first);

		// make all possible init.length()-k+1 flips
		for (int i = 0; i < init.length() - k + 1; i++) {
			std::string s = flip(p.first, k, i);
			if (!seen.count(s)) {
				q.push(std::make_pair(s, p.second + 1));
			}
		}
	}
	return -1;
}

int main(int argc, char** argv) {
	std::ifstream infile(argv[1], std::ifstream::in);

	int t;
	infile >> t;

	for (int i = 1; i <= t; i++) {
		std::string s;
		int k;

		infile >> s >> k;

		const int& moves = search(s, k);
		std::cout << "Case #" << i << ": ";
		if (moves == -1)
			std::cout << "IMPOSSIBLE" << std::endl;
		else
			std::cout << moves << std::endl;
	}
	return 0;
}

