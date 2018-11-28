#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
 
#define ECHO(x) std::cout << x << std::endl;
#define TRACE(x) std::cout << (#x) << " = " << (x) << std::endl;

struct Values {
	long N, R, O, Y, G, B, V;
};

std::string parse(Values& v) {
	std::string result;
	long N = v.N;
	std::unordered_map<char, long> map = {
		{'R', v.R},
		{'Y', v.Y},
		{'B', v.B},
		{'O', v.O},
		{'G', v.G},
		{'V', v.V},
	};
	std::unordered_set<char> choices = {'R', 'Y', 'B', 'O', 'G', 'V'};
	for (auto& pair : map) {
		if (pair.second > 0) {
			result += pair.first;
			pair.second--;
			N--;
			break;
		}
	}

	while (N > 0) {
		char last = result.back();
		auto copy = choices;
		copy.erase(last);

		char max_char;
		long max_amount = -1;
		for (char c : copy) {
			if (map[c] > max_amount) {
				max_char = c;
				max_amount = map[c];
			}
		}

		if (max_amount == 0) return "IMPOSSIBLE";

		result += max_char;
		map[max_char]--;
		N--;
	}

	if (result.back() == result.front()) return "IMPOSSIBLE";

	return result;
}

int main(int, char**) {
	size_t T, i = 0;
	Values v;

	std::cin >> T;
	for (size_t i = 0; i < T; i++) {
		std::cin >> v.N >> v.R >> v.O >> v.Y >> v.G >> v.B >> v.V;
		auto answer = parse(v);
		std::cout << "Case #" << (i+1) << ": " << answer << std::endl;
	}
}
