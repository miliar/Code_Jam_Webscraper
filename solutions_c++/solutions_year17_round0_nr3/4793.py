#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <utility>
#include <sstream>
#include <map>
#include <queue>


using namespace std;

auto solve(long long n, long long k) {
	map<long long, long long> pq;
	pq[n] = 1;
	for (;;) {
		auto end = pq.end();
		--end;
		auto p = *end;
		auto v = p.first;
		if (k <= p.second) {
			return make_pair((v - 1) / 2, v - 1 - (v - 1) / 2);
		}
		auto a = (v - 1) / 2;
		auto b = v - 1 - (v - 1) / 2;
		if (a) {
			pq[a] += p.second;
		}
		if (b) {
			pq[b] += p.second;
		}
		k -= p.second;
		pq.erase(end);
	}
	return make_pair(-1LL, -1LL);
}


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tcs;
	cin >> tcs;
	for (int i = 1; i <= tcs; ++i) {
		long long n;
		long long k;
		cin >> n >> k;
		auto res = solve(n, k);
		cout << "Case #" << i << ": " << res.second << " " << res.first << endl;
	}

	return 0;
}

