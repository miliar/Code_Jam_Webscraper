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


int go(int n, int start, int k) {
	auto getNeighbors = [n, k](int u) {
		vector<int> neighbors;
		for (int i = 0; i < n - k + 1; i++) {
			int v = u;
			for (int j = i; j < i + k; j++) {
				v ^= (1 << j);
			}
			neighbors.push_back(v);
		}
		return neighbors;
	};
	vector<int> D((size_t)1 << n, -1);
	queue<int> Q;
	Q.push(start);
	D[start] = 0;
	while (!Q.empty()) {
		auto u = Q.front();
		if (u == 0) {
			return D[u];
		}
		Q.pop();
		for (auto v : getNeighbors(u)) {
			if (D[v] == -1) {
				D[v] = D[u] + 1;
				Q.push(v);
			}
		}
	}
	return -1;
}
void Go() {
	string s;
	cin >> s;
	int k;
	cin >> k;
	int start = 0;
	for (size_t i = 0; i < s.size(); i++) {
		if (s[i] == '-') {
			start |= (1 << i);
		}
	}
	int res = go((int)s.size(), start, k);
	if (res == -1) {
		cout << "IMPOSSIBLE" << endl;
	}
	else {
		cout << res << endl;
	}
}

int main() {
	const string task = "A";
	const string folder = "gcj/2017/qual";
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
