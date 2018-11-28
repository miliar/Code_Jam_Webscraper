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
	double d;
	int n;
	cin >> d >> n;
	double time = 0;
	for (int i = 0; i < n; i++) {
		double k, v;
		cin >> k >> v;
		double delta = d - k;
		double i_time = delta / v;
		if (i_time > time) time = i_time;
	}
	cout << fixed << std::setprecision(6) 
          << setfill('0')  << (d / time);
}

int main() {
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve(i);
		cout << endl;
	}
}
