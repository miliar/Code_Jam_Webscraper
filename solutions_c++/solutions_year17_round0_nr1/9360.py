#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <utility>
#include <map>

using namespace std;

void solve(string &s, int k) {
	int count = 0;	
	
	auto index = find(s.begin(), s.end(), '-');
	while(index != s.end()) {
		int i = 0;
		for(i = 0; i < k && index != s.end(); ++i, ++index) {
			*index = (*index == '-') ? '+' : '-';
		}
		if(i < k && index == s.end()) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
		++count;
		index = find(s.begin(), s.end(), '-');
	}

	cout << count << endl;
}

int main() {
	int t = 0;
	cin >> t;
	for(int i = 0; i < t; i++) {
		string s;
		int k;
		cin >> s >> k;
		cout << "Case #" << (i+1) << ": ";
		solve(s, k);
	}
	return 0;
}
