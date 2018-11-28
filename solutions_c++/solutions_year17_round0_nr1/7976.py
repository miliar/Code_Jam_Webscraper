#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <iomanip>
#include <string>
#include <sstream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <stack>
using namespace std;

vector<int> flips;
int k;

int numflips(int x) {
	int ans = 0;
	for (int i = 0; i < flips.size(); i++) {
		if (x - flips[flips.size()-1-i] < k) {
			ans++;
		} else {
			break;
		}
	}
	return ans;
}

int main() {
	int t;
	cin >> t;
	for (int tc = 0; tc < t; tc++) {
		flips.clear();
		string s;
		cin >> s;
		cin >> k;
		int res = 0;
		for (int i = 0; i <= s.size()-k; i++) {
			int f = numflips(i);
			if ((s[i] == '+' && f % 2 == 0) || (s[i] == '-' && f % 2 == 1)) {
				continue;
			}
			flips.push_back(i);
			res++;
		}
		// see if rest of pancakes are happy
		bool ok = true;
		for (int i = s.size()-k+1; i < s.size(); i++) {
			int f = numflips(i);
			if ((s[i] == '+' && f % 2 == 1) || (s[i] == '-' && f % 2 == 0)) {
				ok = false;
				break;
			}
		}
		if (!ok) {
			cout << "Case #" << tc+1 << ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << tc+1 << ": " << res << endl;
		}
	}
}















