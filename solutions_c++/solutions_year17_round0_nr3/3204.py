#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;

typedef long long int lld;

void solve_case() {
	lld n, k, done=0;
	map<lld, lld> m;
	cin >> n >> k;
	m[n] = 1;
	while (done < k) {
		map<lld, lld>::iterator it = m.end();
		it--;
		//cout << it->first << " " << it->second << endl;
		done += it->second;
		if (done >= k) {
			cout << it->first / 2 << " " << (it->first-1) / 2 << endl;
			return;
		}
		m[it->first/2] += it->second;
		m[(it->first-1)/2] += it->second;
		m.erase(it);
	}
}

int main() {
	int te;
	cin >> te;
	for (int tt=1; tt<=te; tt++) {
		cout << "Case #" << tt << ": ";
		solve_case();
	}
}

