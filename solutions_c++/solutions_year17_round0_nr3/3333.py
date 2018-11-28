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
#include <functional>
using namespace std;
typedef long long LL;
template<class T> T Abs(T x) { return x < 0 ? -x : x; }


pair<LL, LL> getQ(LL x) {
	if (x % 2 == 0) {
		return {x / 2, x / 2 - 1};
	}
	else {
		return {x / 2, x / 2};
	}
}
void Go() {
	LL n, k;
	cin >> n >> k;
	map<LL, LL, greater<LL>> segments;
	segments[n] = 1;
	LL lastSegmentLength = 0;
	while (k > 0) {
		auto it = segments.begin();
		auto segmentLength = it->first;
		lastSegmentLength = segmentLength;
		auto segmentCount = it->second;
		auto s = min(segmentCount, k);
		segmentCount -= s;
		k -= s;
		if (segmentCount == 0) {
			segments.erase(it);
		}
		auto leftLength = (segmentLength - 1) / 2;
		auto rightLegth = segmentLength / 2;
		segments[leftLength] += s;
		segments[rightLegth] += s;
	}
	auto res = getQ(lastSegmentLength);
	cout << res.first << ' ' << res.second << endl;
}

int main() {
	const string task = "C";
	const string folder = "gcj/2017/qual";
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
			ss << "-small-2-attempt" << attempt;
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
