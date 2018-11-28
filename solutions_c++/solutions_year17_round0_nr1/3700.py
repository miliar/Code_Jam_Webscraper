#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <forward_list>
#include <list>
#include <vector>
#include <bitset>
#include <chrono>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <deque>
#include <stack>
#include <limits>
#include <algorithm>
#include <numeric>
#include <utility>
#include <random>
#include <complex>
#include <tuple>
#include <functional>

using namespace std;


bool flip(string & s, int i, int k) {
	if (i + k > s.size()) return false;
	for (int j = i; k > 0; j++, k--) {
		if (s[j] == '-') s[j] = '+';
		else s[j] = '-';
	}
	return true;
}

int solve(string & s, int k) {
	int count = 0;
	bool inside = false;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '+') continue;
		if (!flip(s, i, k)) return -1;
		count++;
	}
	return count;
}

int main() {
	int t; cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << (i + 1) << ": ";
		string s;
		int k;
		cin >> s;
		cin >> k;
		int res = solve(s, k);
		if (res == -1) cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;
	}
	return 1;
}
