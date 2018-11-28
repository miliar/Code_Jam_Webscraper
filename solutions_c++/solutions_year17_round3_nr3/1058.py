#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <forward_list>
#include <list>
#include <vector>
#include <bitset>
#include <chrono>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <deque>
#include <stack>
#include <limits>
#include <algorithm>
#include <numeric>
#include <utility>
#include <random>
#include <complex>
#include <tuple>
#include <functional>
#include <iomanip>

using namespace std;


void solve(int ti) {
	int n, k;
	cin >> n >> k;
	double u;
	cin >> u;
	vector<double> ps(n);
	for (auto & p : ps) cin >> p;
	sort(ps.begin(), ps.end());
	for (int i = 1; i < n; i++) {
		if (ps[i - 1] < ps[i]) {
			double diff = ps[i] - ps[i - 1];
			double add;
			if (diff * i > u) add = u / i;
			else add = diff;
			u -= add * i;
			for (int j = 0; j < i; j++) ps[j] += add;
		}
	}
	for (int j = 0; j < n; j++) ps[j] += u / n;
	double tp = ps[0];
	for (int j = 1; j < n; j++) tp *= ps[j];
	cout << fixed << setprecision(6) <<  tp;
}

int main() {
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve(i);
		cout << endl;
	}
}
