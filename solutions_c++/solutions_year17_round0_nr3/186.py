#include <iostream>
#include <map>

int main() {
	int t;
    std::cin >> t;
	std::map<long long, long long, std::greater<long long>> m;
    for (int testCase = 1; testCase <= t; testCase++) {
		long long n, k;
		std::cin >> n >> k;
		m.emplace(n, 1);
		long long minlr, maxlr;
		while (k > 0) {
			auto it = m.begin();
			minlr = (it->first - 1) / 2;
			maxlr = it->first / 2;
			m[minlr] += it->second;
			m[maxlr] += it->second;
			k -= it->second;
			m.erase(it);
		}
		m.clear();
		std::cout << "Case #" << testCase << ": ";
		std::cout << maxlr << ' ' << minlr << std::endl;
    }
    return 0;
}
