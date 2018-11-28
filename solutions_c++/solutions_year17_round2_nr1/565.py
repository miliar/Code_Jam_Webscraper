#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:16777216")
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <string>
#include <cassert>
#include <iomanip>
#include <sstream>
#include <iostream>
using namespace std;
typedef long long LL;
template<class T> T Abs(T x) { return x < 0 ? -x : x; }


void Go() {
	LL D, N;
	cin >> D >> N;
	vector<LL> K(N), S(N);
	for (int i = 0; i < N; i++) {
		cin >> K[i] >> S[i];
	}
	auto ok1 = [&](LL k, LL s, double speed) {
		if (s > speed) {
			return true;
		}
		return speed * k / (speed - s) >= D;
	};
	auto ok = [&](double speed) {
		for (int i = 0; i < N; i++) {
			if (!ok1(K[i], S[i], speed)) {
				return false;
			}
		}
		return true;
	};

	double L = 0;
	double R = 1e20;
	for (int i = 0; i < 200; i++) {
		auto M = (L + R) / 2;
		if (ok(M)) {
			L = M;
		}
		else {
			R = M;
		}
	}
	cout << fixed << setprecision(15) << L << endl;
}

int main() {
	const string task = "A";
	const string folder = "gcj/2017/1B";
	const int attempt = -1;
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
