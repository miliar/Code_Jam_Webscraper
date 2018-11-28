#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

#ifdef OLYMP_HXLOCAL
	#define P(expr) (cerr << "[line " << __LINE__ << "] " << #expr << ": " << expr << '\n')
#else
	#define P(expr)
#endif

#define len(arr) ((int)(arr).size())

typedef long long ll;

void solve() {
	ll D;
	int N;
	cin >> D >> N;
	double last_horse_arrival = 0;
	for (int i = 0; i < N; i++) {
		ll K, S;
		cin >> K >> S;
		last_horse_arrival = max(last_horse_arrival, (double) (D - K) / S);
	}

	cout.precision(8);
	cout << fixed;
	cout << D / last_horse_arrival << '\n';
}

int main() {
#ifndef OLYMP_HXLOCAL
	cin.tie(0);
	ios_base::sync_with_stdio(false);
#endif

	int T;
    cin >> T;
    for (int no = 1; no <= T; no++) {
		cout << "Case #" << no << ": ";
		solve();
	}
	return 0;
}
