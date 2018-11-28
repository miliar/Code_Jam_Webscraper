#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

string f() {
	string s; cin >> s;
	vector<int> v;
	for (auto c: s)
		v.push_back(c == '+');
	int k; cin >> k;
	int y = 0;
	for (int i = 0; i + k <= s.size(); ++i) {
		if (!v[i]) {
			for (int j = i; j < i+k; ++j)
				v[j] = !v[j];
			//for (auto x: v) cout << x; cout << endl;
			++y;
		}
	}
	for (int i = 1; i < k; ++i)
		if (!v[s.size() - i])
			return "IMPOSSIBLE";
	return to_string(y);
}

int main() {
	int t; cin >> t;
	for (int x = 0; x < t; ++x)
		cout << "Case #" << x+1 << ": " << f() << endl;
}
