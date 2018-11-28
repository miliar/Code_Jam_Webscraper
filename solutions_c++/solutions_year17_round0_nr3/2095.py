#include <iostream>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>

using namespace std;

#define REP(i, n) for(int i(0); i < (int)(n); i++)
#define FOR(i, a, b) for (int i(a); i <= (int)(b); i++)

void Work(int casen) {
	long long n, k;
	cin >> n >> k;
	map<long long, long long> a;
	a[-n] = 1;
	while (k != 0) {
		long long x = -a.begin()->first;
		long long y = a.begin()->second;
		if (k <= y) {
			n = x;
			break;
		}
		k -= y;
		a[-((x - 1) / 2)] += y;
		a[-((x - 0) / 2)] += y;
		a.erase(-x);
	}
	long long x = (n / 2), y = (n - 1) / 2;
	cout << "Case #" << casen << ": " << max(x, y) << ' ' << min(x, y) << endl;
}

int main() {
	int n;
	cin >> n;
	FOR(i, 1, n) {
		Work(i);
	}
	return 0;
}