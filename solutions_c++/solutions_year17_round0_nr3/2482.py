#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <set>

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;

map<int64, map<pair<int64, int64>, int64>> a;

void calc(int64 n) {
	if (a.find(n) != a.end()) return;
	int64 left = (n - 1)/ 2;
	int64 right = n - 1 - left;
	calc(left);
	calc(right);
	for (auto it = a[left].begin(); it != a[left].end(); ++it) {
		a[n][it->first] += it->second;
	}
	
	for (auto it = a[right].begin(); it != a[right].end(); ++it) {
		a[n][it->first] += it->second;
	}
	a[n][mp(left, right)] += 1;
	
}

void solve() {
    int64 n, k;
	cin >> n >> k;
	a.clear();
	map<pair<int64, int64>, int64> base;
	base[mp(0, 0)] = 1;
	a[0] = map<pair<int64, int64>, int64>();
	a[1] = base;
	calc(n);
	auto it = a[n].end();
	--it;
	int64 sum = 0;
	while (true) {
		sum += it->second;
		if (sum >= k) {
			cout << it->first.second << " " << it->first.first << endl; 
			break;
		}
		--it;
	}
}   

int main() {
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
