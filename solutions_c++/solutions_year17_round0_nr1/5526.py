#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <stdexcept>
#include <functional>
#include <math.h>
#include <utility>
#include <sstream>
#pragma comment(linker, "/STACK:133217728")

using namespace std;

const int INF = 1e+9;
int solve(string s, int k) {
	int ans = 0;
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == '-' && i + k > s.length()) {
			return INF;
		}
		if (s[i] == '-') {
			for (int j = i; j < i + k; j++)
				s[j] = s[j] == '+' ? '-' : '+';
			ans++;
		}
	}
	return ans;
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	ios_base::sync_with_stdio(0);
	
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int k;
		string s;
		cin >> s >> k;
		cout << "Case #" << t << ": ";
		int ans = solve(s, k);
		if (ans == INF)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
	return 0;
}
