#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

inline void Apply(size_t pos, size_t k, string& s) {
	for (k += pos; pos < k; ++pos)
		s[pos] = !s[pos];
}

inline int Pancakes(string& s, size_t k) {
	size_t last = s.size() - k + 1;
	size_t count = 0;
	for (size_t i = 0; i < last; ++i) {
		if (!s[i]) {
			Apply(i, k, s);
			count++;
		}
	}
	for (size_t i = last; i < s.size(); ++i) {
		if (!s[i])
			return -1;
	}
	return (int)count;
}

int main() {
	int testCount;
	string test;
	cin >> testCount;
	for (int i = 1; i <= testCount; ++i) {
		cin >> test;
		int k;
		cin >> k;
		for (auto &c : test)
			c = (c == '+');
		int result = Pancakes(test, k);
		cout << "Case #" << i << ": ";
		if (result >= 0)
			cout << result;
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}
    return 0;
}
