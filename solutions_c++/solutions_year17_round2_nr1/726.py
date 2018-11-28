#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <iomanip>

using namespace std;

#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)

typedef pair<int, int> pii;
typedef long long ll;

const int MAX = 1000000;

void solve() {
	ll D, N;
	cin >> D >> N;
	double time = 0;
	REP(i, N) {
		ll K, S;
		cin >> K >> S;
		double cur = ((double)(D - K)) / S;
		time = max(time, cur);
	}
	cout << D / time;
}

int main() {
	int t;
	cin >> t;
	cout << fixed << setprecision(10);
	REP(i, t) {
		cout << "Case #" << (i+1) << ": ";
		solve();
		cout << endl;
	}
}