#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <cfloat>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>

#define MOD 1000000007
#define PI 3.14159265359
#define REP(i,n) for(int i = 0; i < n; ++i)
#define FOR(i,n,m) for(int i = n; i < m; ++i)
#define ll long long

using namespace std;

bool flip(string &s, int idx, int k) {
	for (int i=0; i<k; ++i) {
		if (idx + i >= s.size()) return false;
		s[idx+i] = (s[idx+i] == '+') ? '-' : '+';
	}
	return true;
}

int func(string  &s, int k) {
	int ans = 0;
	for (int idx = 0; idx < s.size(); ++idx) {
		if (s[idx] == '+') continue;
		if (!flip(s, idx, k)) return -1;
		++ans;
	}
	return ans;
}

int main() {
	int t, k;
	string str;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> str;
		cin >> k;
		int ans = func(str, k);
		if (ans == -1)
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
