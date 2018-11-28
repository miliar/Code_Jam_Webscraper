#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
	int T;
	cin >> T;
	string s;
	int k;
	for(int t = 1; t <= T; ++t) {
		cin >> s >> k;
		int n = s.size(), ans = 0;
		for (int i = 0; i + k - 1 < n; ++i) {
			if(s[i] == '-') {
				for(int j = i; j < i + k; ++j) {
					s[j] = s[j] == '-' ? '+' : '-';
				}
				++ans;
			}
		}
		bool done = true;
		for(int i = 0; i < n; ++i) {
			if(s[i] == '-') {
				done = false;
				break;
			}
		}
		if(done)
			cout << "Case #" << t << ": " << ans << endl;
		else
			cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
	}
}