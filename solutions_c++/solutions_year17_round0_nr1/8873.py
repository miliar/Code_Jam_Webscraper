#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<bool> parse(string s) {
	vector<bool> v(s.length());
	for (int i = 0; i<s.length(); i++) {
		v[i] = s.at(i) == '+';
	}
	return v;
}

int rec(int pos, vector<bool> pancakes, int needed, int k) {
	if (pos+k > pancakes.size()) {
		for (int i = pos; i<pancakes.size(); i++) {
			if (! pancakes[i]) {
				return -1;
			}
		}
		return needed;
	}
	if (! pancakes[pos]) {
		needed++;
		for (int i = pos; i<pos+k; i++) {
			pancakes[i] = ! pancakes[i];
		}
	}
	return rec(pos+1, pancakes, needed, k);
}

int main() {
	int t, k;
	cin >> t;
	for (int i = 0; i<t; i++) {
		string s;
		cin >> s >> k;
		vector<bool> b = parse(s);
		int needed = rec(0, b, 0, k);
		cout << "Case #" << i+1 << ": ";
		if (needed >= 0) {
			cout << needed;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
}