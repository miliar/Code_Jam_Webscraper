#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:16777216")
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <string>
#include <cassert>
#include <sstream>
#include <iostream>
using namespace std;
typedef long long LL;
template<class T> T Abs(T x) { return x < 0 ? -x : x; }


void Go() {
	int n, R, O, Y, G, B, V;
	cin >> n >> R >> O >> Y >> G >> B >> V;
	string s;
	auto ok = [n](const string& s) {
		int n = s.size();
		for (int i = 0; i < n; i++) {
			if (s[i] == s[(i + 1) % n]) {
				return false;
			}
		}
		return true;
	};
	vector<int> cnt {R, Y, B};
	if (R + Y + B != n) {
		throw 42;
	}
	string colors = "RYB";
	int lastC = 0;
	while (s.size() < n) {
		if (cnt[lastC] > 0) {
			cnt[lastC] -= 1;
			s.push_back(colors[lastC]);
		}
		lastC = (lastC + 1) % 3;
	}
	int t = n * min(100, n);
	while (!ok(s) && t > 0) {
		for (int i = 0; i < n; i++) {
			if (s[i] == s[(i + 1) % n]) {
				if (s[(i + 1) % n] != s[(i + 2) % n]) {
					swap(s[(i + 1) % n], s[(i + 2) % n]);
					continue;
				}
			}
		}
		t--;
	}

	if (s.size() == n && ok(s)) {
		cout << s << endl;
	}
	else {
		cout << "IMPOSSIBLE" << endl;
	}
}

int main() {
	const string task = "B";
	const string folder = "gcj/2017/1B";
	const int attempt = 0;
	const bool dbg = false;

	if (dbg) {
		freopen("inp.txt", "r", stdin);
	}
	else {
		stringstream ss;
		ss << folder << '/' << task;
		if (attempt < 0)
			ss << "-large";
		else
			ss << "-small-attempt" << attempt;
		freopen((ss.str() + ".in").c_str(), "r", stdin);
		freopen((ss.str() + ".out").c_str(), "w", stdout);
	}
	ios_base::sync_with_stdio(false);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		Go();
	}
	return 0;
}
