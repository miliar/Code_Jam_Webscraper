#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iomanip>

using namespace std;
typedef unsigned long long ull;

void solve() {
	int n,p;
	cin >> n >> p;
	int groups[5] = {0};
	for (int i=0; i<n; ++i) {
		int tmp;
		cin >> tmp;
		groups[p-(tmp%p)] +=1;
	}
	int ans = groups[p];

	for (int i=1; i<p; ++i) {
		while (groups[i] && groups[p-i]) {
			if (i==p-i && groups[i] == 1) break;
			++ans;
			--groups[i];
			--groups[p-i];
		}
	}
	int rest = 0;
	for (int i=1; i<p; ++i) {
		while (groups[i]) {
			//cout << i << " " << rest << endl;
			if (rest == 0) {
				++ans;
			}
			rest = (i+rest)%p;
			--groups[i];
		}
	}
	cout << ans << endl;

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
