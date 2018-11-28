#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;

using Integer = long long;

std::pair<Integer, Integer>
experiment(Integer n, Integer k) {
	map<Integer, Integer> m;

	m[n] = 1;	

	while (true) {
		auto iterator = m.rbegin();
		Integer a = iterator->first;
		auto count = iterator->second;
		if (k <= count) return {a/2, a-(a/2)-1};
		k -= count;
		m.erase(a);
		m[a/2] += count;
		m[a-(a/2)-1] += count;
	}
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		std::cerr << "i=" << i << std::endl;
		Integer n, k;
		cin >> n >> k;
		auto p = experiment(n, k);
		cout << "Case #" << i << ": " << p.first << " " << p.second << endl;

	}

	return 0;
}
