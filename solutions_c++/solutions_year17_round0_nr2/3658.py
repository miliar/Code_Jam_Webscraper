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

int not_tidy_index(string & n) {
	for (int i = 1; i < n.size(); i++) {
		if (n[i] < n[i - 1]) return i;
	}
	return n.size();
}

string solve(string & n) {
	int n_i = not_tidy_index(n);
	if (n_i == n.size()) return n;
	while (n_i > 0 && n[n_i] - 1 < n[n_i - 1]) n_i--;
	string res;
	for (int i = 0; i < n_i; i++) {
			res.push_back(n[i]);
	}
	res.push_back(n[n_i] - 1);
	for (int i = n_i + 1; i < n.size(); i++) {
		res.push_back('9');
	}
	if (res[0] == '0') res.erase(res.begin());
	return res;
}

int main() {
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		string s; cin >> s;
		cout << solve(s) << endl;
	}	
}