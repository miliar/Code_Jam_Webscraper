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

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		double D;
		ll N;
		cin >> D >> N;
		double K, S;
		double tmax = 0;
		for (int j = 0; j < N; j++) {
			cin >> K >> S;
			double t = (D - K) / S;
			if (t > tmax) tmax = t;
		}
		cout << "Case #" << i << ": " << fixed << setprecision(12) << D / tmax << endl;
	}

	return 0;
}