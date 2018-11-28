#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
#include <tuple>
#include <queue>
#include <utility>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <limits>
#include <new>
#include <functional>
#include <unordered_map>
#include <unordered_set>
#include <random>
#include <chrono>
#include <thread>

const double pi = 3.1415926535897932384626433832795;

using namespace std;

typedef long long ll;

int main(void) {
	cin.tie(nullptr);
	cin.sync_with_stdio(false);

	vector<ll> pws = { 0 };
	ll temp = 1;
	for (ll i = 0; i < 62; i++) {
		temp *= 2;
		pws.push_back(temp - 1);
	}

	int t;
	cin >> t;
	for (int c = 1; c <= t; c++) {
		ll N, K;
		cin >> N >> K;
		ll L, R;
		auto tmp = upper_bound(pws.begin(), pws.end(), K);
		ll temp = *(tmp - 1);
		if (temp == K) temp = *(tmp - 2);
		ll T = N - temp;
		ll TT = T / (temp + 1);
		ll TTT = T % (temp + 1);
		if (TTT >= K - temp) {
			L = TT / 2;
			R = (TT + 1) / 2;
		}
		else {
			L = (TT - 1) / 2;
			R = TT / 2;
		}
		cout << "Case #" << c << ": " << (L > R ? L : R) << " " << (L < R ? L : R) << "\n";
	}

	return 0;
}