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
	int n, p;
	cin >> n >> p;
	vector<int> g;	
	vector<int> cnt(p);
	for (int i = 0; i < n; i++) {
		int v;
		cin >> v;
		v = v % p;
		cnt[v] += 1;
	}
	int res = cnt[0];
	if (p == 2) {
		res += (cnt[1] + 1) / 2;
	}
	else if (p == 3) {
		int d = min(cnt[1], cnt[2]);
		res += d;
		cnt[1] -= d;
		cnt[2] -= d;
		if (cnt[1] > 0) {
			res += (cnt[1] + 2) / 3;
		}
		else {
			res += (cnt[2] + 2) / 3;
		}
	}
	else {
		throw 42;
	}
	cout << res << endl;
}

int main() {
	const string task = "A";
	const string folder = "gcj/2017/2";
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
