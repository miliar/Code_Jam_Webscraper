#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <string>
using namespace std;

typedef long long ll;

bool checkTwo(char f, char s) {
	bool b = true;
	switch (f) {
	case 'R':
		b = ((string("VRO")).find(s) == string::npos);
		break;
	case 'O':
		b = ((string("ROY")).find(s) == string::npos);
		break;
	case 'Y':
		b = ((string("OYG")).find(s) == string::npos);
		break;
	case 'G':
		b = ((string("YGB")).find(s) == string::npos);
		break;
	case 'B':
		b = ((string("GBV")).find(s) == string::npos);
		break;
	case 'V':
		b = ((string("BVR")).find(s) == string::npos);
		break;
	}
	return b;
}

bool check(string & s) {
	for (int i = 0; i < s.size(); ++i) {
		if (!checkTwo(s[i], s[(i + 1) % ((int)(s.size()))])) {
			return false;
		}
	}
	return true;
}

void solve() {
	int n;
	int r, o, y, g, b, v;
	int R, O, Y, G, B, V;
	cin >> n;
	cin >> R >> O >> Y >> G >> B >> V;
	string ans;
	char l = 'R';
	r = R;
	o = O;
	y = Y;
	g = G;
	b = B;
	v = V;
	while (r + y + b) {
		switch (l) {
		case 'R':
			if (b > y) {
				ans.push_back('B');
				l = 'B';
				--b;
			} else {
				if (y > 0) {
					ans.push_back('Y');
					l = 'Y';
					--y;
				} else {
					l = 'Y';
				}
			}
			break;
		case 'Y':
			if (r > b) {
				ans.push_back('R');
				l = 'R';
				--r;
			} else {
				if (b > 0) {
					ans.push_back('B');
					l = 'B';
					--b;
				} else {
					l = 'B';
				}
			}
			break;
		case 'B':
			if (y > r) {
				ans.push_back('Y');
				l = 'Y';
				--y;
			} else {
				if (r > 0) {
					ans.push_back('R');
					l = 'R';
					--r;
				} else {
					l = 'R';
				}
			}
			break;
		}
	}
	if (check(ans)) {
		cout << ans;
		return;
	}
	ans = "";
	l = 'Y';
	r = R;
	o = O;
	y = Y;
	g = G;
	b = B;
	v = V;
	while (r + y + b) {
		switch (l) {
		case 'R':
			if (b > y) {
				ans.push_back('B');
				l = 'B';
				--b;
			}
			else {
				if (y > 0) {
					ans.push_back('Y');
					l = 'Y';
					--y;
				}
				else {
					l = 'Y';
				}
			}
			break;
		case 'Y':
			if (r > b) {
				ans.push_back('R');
				l = 'R';
				--r;
			}
			else {
				if (b > 0) {
					ans.push_back('B');
					l = 'B';
					--b;
				}
				else {
					l = 'B';
				}
			}
			break;
		case 'B':
			if (y > r) {
				ans.push_back('Y');
				l = 'Y';
				--y;
			}
			else {
				if (r > 0) {
					ans.push_back('R');
					l = 'R';
					--r;
				}
				else {
					l = 'R';
				}
			}
			break;
		}
	}
	if (check(ans)) {
		cout << ans;
		return;
	}
	ans = "";
	l = 'B';
	r = R;
	o = O;
	y = Y;
	g = G;
	b = B;
	v = V;
	while (r + y + b) {
		switch (l) {
		case 'R':
			if (b > y) {
				ans.push_back('B');
				l = 'B';
				--b;
			}
			else {
				if (y > 0) {
					ans.push_back('Y');
					l = 'Y';
					--y;
				}
				else {
					l = 'Y';
				}
			}
			break;
		case 'Y':
			if (r > b) {
				ans.push_back('R');
				l = 'R';
				--r;
			}
			else {
				if (b > 0) {
					ans.push_back('B');
					l = 'B';
					--b;
				}
				else {
					l = 'B';
				}
			}
			break;
		case 'B':
			if (y > r) {
				ans.push_back('Y');
				l = 'Y';
				--y;
			}
			else {
				if (r > 0) {
					ans.push_back('R');
					l = 'R';
					--r;
				}
				else {
					l = 'R';
				}
			}
			break;
		}
	}
	if (check(ans)) {
		cout << ans;
		return;
	}
	cout << "IMPOSSIBLE";
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nT;
	cin >> nT;
	for (int i = 0; i < nT; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}