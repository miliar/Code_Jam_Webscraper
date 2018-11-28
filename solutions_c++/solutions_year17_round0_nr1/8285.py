#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

unsigned t, k;
string s;

void flip(string& s, unsigned i) {
	s[i] = (s[i] == '+') ? '-' : '+';
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	cin >> t;
	for (unsigned cas = 1; cas <= t; cas++) {
		cin >> s >> k;
		string goal(s.size(), '+');
		int result = -1;
		queue<pair<int,string>> Q;
		set<string> v;
		Q.push({ 0, s });
		while (!Q.empty()) {
			auto now = Q.front();
			Q.pop();
			if (v.insert(now.second).second == false) 
				continue;
			if (now.second == goal) {
				result = now.first;
				break;
			}
			string next = now.second;
			for (unsigned i = 0; i < k; i++) {
				flip(next, i);
			}
			Q.push({ now.first + 1, next });
			for (unsigned i = k; i < s.size(); i++) {
				flip(next, i - k);
				flip(next, i);
				Q.push({ now.first + 1, next });
			}
		}
		if (result == -1)
			cout << "Case #" << cas << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << cas << ": " << result << endl;
	}
	return 0;
}