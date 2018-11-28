#include <iostream>
#include <set>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		int n, k, a, b;
		cin >> n >> k;
		multiset<int> s;
		s.insert(n);
		for (int j = 0; j < k; ++j) {
			auto it = --s.end();
			int x = *it;
			s.erase(it);
			it = s.insert(b = (x - 1) / 2);
			s.insert(it, a = x / 2);
		}
		cout << "Case #" << i << ": " << a << " " << b << endl;
	}
}
