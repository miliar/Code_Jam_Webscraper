#include <stdio.h>
#include <algorithm>
#include <string>
#include <sstream>
#include <queue>
#include <map>
#include <tuple>
#include <iostream>

using namespace std;

void solve() {
	int n, r, o, y, g, b, v;
	cin >> n >> r >> o >> y >> g >> b >> v;
	r -= g;
	y -= v;
	b -= o;

	string result;
	vector<tuple<int, int, int>> pq;
	int mx = max(max(r, y), b);
	pq.emplace_back(r, r == mx, 'R');
	pq.emplace_back(y, y == mx, 'Y');
	pq.emplace_back(b, b == mx, 'B');
	int m = r + y + b;
	for (int j = 0; j < m; ++j) {
		int best = -1;
		for (int i = 0; i < 3; ++i)
			if (result.empty() || result.back() != get<2>(pq[i])) {
				if (best == -1 || pq[best] < pq[i])
					best = i;
			}
		if (best == -1 || get<0>(pq[best]) == 0) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
		get<0>(pq[best])--;
		result += get<2>(pq[best]);
	}
	if (result.size() && result.front() == result.back()) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	string output;
	for (char ch : result) {
		if (ch == 'R' && g) {
			output += "RGR";
			--g;
		}
		else if (ch == 'R') {
			output += ch;
		}
		if (ch == 'Y' && v) {
			output += "YVY";
			--v;
		}
		else if (ch == 'Y') {
			output += ch;
		}
		if (ch == 'B' && o) {
			output += "BOB";
			--o;
		}
		else if (ch == 'B') {
			output += ch;
		}
	}
	if (g || v || o) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	cout << output << endl;
}

#define DIR "C:/Users/dmarin3/Downloads/"
#define PROBLEM "B"

//#define LARGE
//#define TEST

int main() {
#ifdef LARGE
	freopen(DIR PROBLEM "-large.in", "rt", stdin);
#elif defined(TEST)
	freopen("input.txt", "rt", stdin);
#else
	freopen(DIR PROBLEM "-small-attempt0.in", "rt", stdin);
#endif
	freopen("output.txt", "wt", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
	}
}
