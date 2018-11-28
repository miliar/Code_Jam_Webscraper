#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

#define uchar unsigned char
#define ushort unsigned short
#define uint unsigned int
#define ull unsigned ll
#define ll long long
#define ull unsigned ll

#define E 2.718281828
#define PI 3.14159265358979323846264338328

using namespace std;

void solve() {
	int n, r, o, y, g, bb, vv;
	cin >> n >> r >> o >> y >> g >> bb >> vv;
	vector<pair<int, char> > v;
	v.push_back(pair<int, char>(r, 'R'));
	v.push_back(pair<int, char>(y, 'Y'));
	v.push_back(pair<int, char>(bb, 'B'));
	sort(v.begin(), v.end());
	int a = v[0].first, b = v[1].first, c = v[2].first;
	char ca = v[0].second, cb = v[1].second, cc = v[2].second;
	if (c - b > a) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	int x = a - (c - b);
	string res;
	while (b) {
		c--, b--;
		res += cc;
		res += cb;
		if (x) {
			x--, a--;
			res += ca;
		}
	}
	while (c) {
		c--, a--;
		res += cc;
		res += ca;
	}
	cout << res << endl;
}

int main() {
	int t, i;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
