#include <iostream>
#include <map>
#include <algorithm>

using namespace std;
typedef unsigned long long ull;

void solve() {
	ull n,k;
	map<ull, ull, greater<ull> > map;
	cin >> n >> k;
	--k;
	map[n] = 1;
	while (k) {
		auto curI = map.begin();
		ull key = curI->first;
		ull count = curI->second;
		count = min(count, k);
		curI->second -= count;

		map[key/2]+=count;
		map[(key-1)/2]+=count;

		k-=count;
		if (map[key] == 0) {
			map.erase(key);
		}
	}
	ull final = map.begin()->first;
	cout << final/2 << " " << (final-1)/2 << endl;
}

int main() {
	int cases;
	cin >> cases;
	for (int i=1; i<=cases; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}